# Managing your Metal app window in iPadOS

**Framework**: Metal

Set up a window that handles dynamically resizing your Metal content.

#### Overview

A scene represents a single instance of your app’s UI. You can choose whether people can create multiple scenes for your app. Typically, Metal apps and games support only one scene because they need priority access to the available resources on a device. On iPadOS 26 and later, people can always resize your app’s scenes if they have enabled multitasking.

Apps that don’t adopt the scene-based life cycle log a warning at startup on iOS 26 and iPadOS 26 and must be updated. In the next major release, the scene-based life cycle is required when building with the latest SDK.

> ❗ **Important**: Because [`UIRequiresFullScreen`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiresFullScreen) is deprecated, you can no longer opt out of iPad multitasking and dynamic resizing.

For more information on migrating your iPad app, see [`TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key`](https://developer.apple.com/documentation/Technotes/tn3192-Migrating-your-app-from-the-deprecated-UIRequiresFullScreen-key) and [`TN3187: Migrating to the UIKit scene-based life cycle`](https://developer.apple.com/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle).

#### Create the Window

Manage windows on iPad by using [`UIWindowScene`](https://developer.apple.com/documentation/UIKit/UIWindowScene) for UIKit and [`Scene`](https://developer.apple.com/documentation/SwiftUI/Scene) for SwiftUI. To configure a [`UIWindow`](https://developer.apple.com/documentation/UIKit/UIWindow) under a scene you assign a content view controller and embed your Metal view inside the controller.

To configure scene support for your Metal project:

1. Open the Xcode project.
2. Select the project in the Project navigator.
3. Select the app target.
4. Navigate to the General tab.
5. In the Deployment Info section, select “Scene manifest”.
6. Add the [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key if it doesn’t already exist.
7. Configure the dictionary value for your project.

To provide dynamic scene configurations for complex scenes that require fine-grained control, implement [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:)) for UIKit and [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/SwiftUI/UIApplicationDelegateAdaptor) for apps that uses the SwiftUI life cycle. This allows for providing dynamic scene configurations:

For more information on dynamic configuration, see [`TN3187: Migrating to the UIKit scene-based life cycle`](https://developer.apple.com/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle#Provide-scene-configurations-from-your-app-delegate-for-dynamic-configuration). For more information on adding scene support to your app, see [`Specifying the scenes your app supports`](https://developer.apple.com/documentation/UIKit/specifying-the-scenes-your-app-supports).

#### Choose the Content Size and Style of Your Window

After adding scene support, configure the initial size and style of your window’s scenes. When your app creates or restores an instance of your user interface, the system calls [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)). This delegate method provides a window scene that you use to configure size contraints and style. For Metal apps and games, this is typically a single scene.

Use [`UISceneSizeRestrictions`](https://developer.apple.com/documentation/UIKit/UISceneSizeRestrictions) to constrain the minimum size you want, and to handle aspect ratio changes:

In SwiftUI, use the [`windowResizability(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/windowResizability(_:)) modifier to allow your scene’s content to provide sizing information:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
               .frame(minWidth: 640, minHeight: 360)
        }
        .windowResizability(.contentMinSize)
    }
}
```

To get the display scale, access [`displayScale`](https://developer.apple.com/documentation/UIKit/UITraitCollection/displayScale) from [`UITraitCollection`](https://developer.apple.com/documentation/UIKit/UITraitCollection) and perform necessary updates in [`viewIsAppearing(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewIsAppearing(_:)). To calculate the pixel values you use for updating the size of [`MTLDrawable`](mtldrawable.md), multiply the view’s frame and the [`contentsScale`](https://developer.apple.com/documentation/QuartzCore/CALayer/contentsScale) of your [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer):

When a person resizes a window, it’s possible that the Metal view only renders to a portion of the window. In this case, add a launch screen with a black background color to letterbox the presentation, then configure the content gravity property for your view so drawable content scales uniformly.

![A screenshot of the Xcode information property list file that shows metadata](https://docs-assets.developer.apple.com/published/30f3a45ffa935ef047fafa4d51ea7b2a/managing-your-metal-app-window-in-ipados-launch-screen-1%402x.png)

#### Handle Window Resizing

When resizing a window, the system sets [`isInteractivelyResizing`](https://developer.apple.com/documentation/UIKit/UIWindowScene/Geometry/isInteractivelyResizing) and calls the scene delegate
[`windowScene(_:didUpdateEffectiveGeometry:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:didUpdateEffectiveGeometry:)) to allow for an app to handle window size changes. When a window resizes, continue rendering at the existing render target size until a person stops resizing the window, at which point you can update the new render target size. Don’t query the window size while a person is resizing a window. Instead, track the state in your renderer and then perform the necessary render size update when the person finishes resizing the window. For more information on responding to scene size changes, see [`TN3187: Migrating to the UIKit scene-based life cycle`](https://developer.apple.com/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle#Provide-scene-configurations-from-your-app-delegate-for-dynamic-configuration).

If you use [`MetalKit`](https://developer.apple.com/documentation/MetalKit), your app receives the [`mtkView(_:drawableSizeWillChange:)`](https://developer.apple.com/documentation/MetalKit/MTKViewDelegate/mtkView(_:drawableSizeWillChange:)) delegate view callback:

Your [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) views receive a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) life cycle call to [`layoutSubviews()`](https://developer.apple.com/documentation/UIKit/UIView/layoutSubviews())
and related property updates — [`contentScaleFactor`](https://developer.apple.com/documentation/UIKit/UIView/contentScaleFactor), [`frame`](https://developer.apple.com/documentation/UIKit/UIView/frame), and [`bounds`](https://developer.apple.com/documentation/UIKit/UIView/bounds). Use the related properties to update the [`MTLDrawable`](mtldrawable.md) size by getting the window scene’s [`bounds`](https://developer.apple.com/documentation/UIKit/UICoordinateSpace/bounds) from [`coordinateSpace`](https://developer.apple.com/documentation/UIKit/UIWindowScene/Geometry/coordinateSpace) and multiplying it by the [`contentsScale`](https://developer.apple.com/documentation/QuartzCore/CALayer/contentsScale) of your [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer):

#### Handle Moving a Window Between Displays

In iPad, you use [`UITraitCollection`](https://developer.apple.com/documentation/UIKit/UITraitCollection) to assist with providing a flexible windowing environment that allows your app to render and move windows between multiple displays. To eliminate the need to manually register for trait changes, use [`Automatic trait tracking`](https://developer.apple.com/documentation/UIKit/automatic-trait-tracking) to observe the values you need from your specific views. In some cases, you might use [`UIScreen`](https://developer.apple.com/documentation/UIKit/UIScreen) to access a trait that [`UITraitCollection`](https://developer.apple.com/documentation/UIKit/UITraitCollection) doesn’t provide, like [`nativeScale`](https://developer.apple.com/documentation/UIKit/UIScreen/nativeScale).

When your app’s scene geometry changes — like when moving between screens — the [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate) calls the [`windowScene(_:didUpdateEffectiveGeometry:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:didUpdateEffectiveGeometry:)) method to inspect the window geometry and perform necessary updates:

For more information on supporting multiple displays in iPadOS, see [`Presenting content on a connected display`](https://developer.apple.com/documentation/UIKit/presenting-content-on-a-connected-display). For more information on managing your Metal app window in macOS, see [`Managing your game window for Metal in macOS`](managing-your-game-window-for-metal-in-macos.md).

#### Lock Interface Orientation for Device Rotation

Some Metal apps and games might need to lock the interface orientation so the screen geometry remains locked when a person rotates the device. To lock the orientation, call [`setNeedsUpdateOfPrefersInterfaceOrientationLocked()`](https://developer.apple.com/documentation/UIKit/UIViewController/setNeedsUpdateOfPrefersInterfaceOrientationLocked()) in your view controller and check whether the interface is already locked with the `previousEffectiveGeometry` parameter of [`windowScene(_:didUpdateEffectiveGeometry:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:didUpdateEffectiveGeometry:)):

For more information on locking your app’s orientation, see [`TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key`](https://developer.apple.com/documentation/Technotes/tn3192-Migrating-your-app-from-the-deprecated-UIRequiresFullScreen-key#Request-scene-orientation-lock).

## See Also

- [Managing your game window for Metal in macOS](managing-your-game-window-for-metal-in-macos.md)
  Set up a window and view for optimally displaying your Metal content.
- [Adapting your game interface for smaller screens](adapting-your-game-interface-for-smaller-screens.md)
  Make text legible on all devices the player chooses to run your game on.
- [Onscreen presentation](onscreen-presentation.md)
  Show the output from a GPU’s rendering pass to the user in your app.
- [HDR content](hdr-content.md)
  Take advantage of high dynamic range to present more vibrant colors in your apps and games.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/managing-your-metal-app-window-in-ipados)*