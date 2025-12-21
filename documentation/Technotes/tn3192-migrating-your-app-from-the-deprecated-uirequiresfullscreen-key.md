# TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key

**Framework**: Technotes

Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.

#### Overview

Prior to iPadOS 26, apps could request a compatibility mode that opted them out of multitasking and dynamic scene resizing through the [`UIRequiresFullScreen`](https://developer.apple.comhttps://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiresFullScreen) key. This key-value pair configures iPadOS apps only, and is ignored for iOS apps.

Update apps that rely on `UIRequiresFullScreen`’s compatibility mode to handle resizing scenes so they can provide a better multitasking experience.

> **Note**: Starting in iPadOS 26, `UIRequiresFullscreen` and its associated compatibility mode are deprecated and will be ignored in a future release. Apps that don’t update may experience broken layouts, UI elements positioned incorrectly, or content that doesn’t fit properly when the system resizes their scenes to accommodate multitasking scenarios they weren’t designed to handle.

This guide will help you migrate away from `UIRequiresFullScreen` and handle dynamic resizing. For more information on the enhanced window resizing and improved multitasking, see WWDC25 session 282: [`Make your UIKit app more flexible`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/282/).

#### Determine If Your App Should Update

To support resizable scenes ensure that your app:

- Provides a [`Specifying your app’s launch screen`](https://developer.apple.com/documentation/Xcode/specifying-your-apps-launch-screen).
- Supports all [`interface orientations`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/layout#Adaptability).
- Doesn’t include the `UIRequiresFullScreen` key in its [`Info.plist`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information-property-list) or [`INFOPLIST_KEY_UIRequiresFullScreen`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/build-settings-reference#Requires-Full-Screen) or its build settings.

With these updates, your app will support resizable scenes and multitasking. To learn more about adopting scene-based life cycle, see [`TN3187: Migrating to the UIKit scene-based life cycle`](tn3187-Migrating-to-the-UIKit-scene-based-life-cycle.md).

#### Respond to Scene Size Changes

If your app layout relies on consistent scene size, or uses absolute values for its view geometry, consider using Auto Layout to calculate the size and position of its views through constraints placed on its views.

By using Auto Layout, you’re able to replace static, frame-based layouts in your app with flexible constraint-based layouts that respond to size changes. For more information on Auto Layout, including layout constraints and attributes, see [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html).

When transitioning away from the deprecated `UIRequiresFullScreen` key, ensure your app’s views adapt to dynamic size changes that occur when users resize windows or change device orientation. Each of these scenarios can cause your app’s scene bounds to change at runtime, potentially breaking layouts that assume fixed dimensions. To learn more about debugging Auto Layout issues, see [`Unsatisfiable Layouts`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/ConflictingLayouts.html#//apple_ref/doc/uid/TP40010853-CH19-SW1).

You can adjust your app’s layout when the environment changes, such as when size class, display scale, or layout direction changes occur. To detect these changes, use [`registerForTraitChanges(_:target:action:)`](https://developer.apple.com/documentation/UIKit/UITraitChangeObservable-67e94/registerForTraitChanges(_:target:action:)) or [`registerForTraitChanges(_:handler:)`](https://developer.apple.com/documentation/UIKit/UITraitChangeObservable-67e94/registerForTraitChanges(_:handler:)) to register a list of traits to observe.

To observe a scene’s geometry changing, use [`windowScene(_:didUpdateEffectiveGeometry:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:didUpdateEffectiveGeometry:)) and compare the `coordinateSpace.bounds` of both geometries.

Additionally, use [`isInteractivelyResizing`](https://developer.apple.com/documentation/UIKit/UIWindowScene/Geometry/isInteractivelyResizing) to handle interactive resizing of the scene specifically. For example:

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var gameAssetManager = MyGameAssetManager()
    var previousSceneSize = CGSize.zero

    func windowScene(
        _ windowScene: UIWindowScene,
        didUpdateEffectiveGeometry previousGeometry: UIWindowScene.Geometry) {

        let geometry = windowScene.effectiveGeometry
        let sceneSize = geometry.coordinateSpace.bounds.size

        if !geometry.isInteractivelyResizing && sceneSize != previousSceneSize {
            previousSceneSize = sceneSize
            gameAssetManager.updateAssets(sceneSize: sceneSize)
        }
    }
}
```

In this example, `isInteractivelyResizing` is queried to only update assets for a new scene size after the interaction finishes. This is helpful for games, where multiple assets may require resizing when the scene changes size or if there are elements of your app’s UI that are computationally expensive to draw.

In SwiftUI, use [`onInteractiveResizeChange(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onInteractiveResizeChange(_:)) to adjust how your view behaves when a window is in the process of being resized by the user.

#### Specify Scene Sizing Preference

To express a preferred minimum size of your scene’s content, use [`UISceneSizeRestrictions`](https://developer.apple.com/documentation/UIKit/UISceneSizeRestrictions). For example:

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    func scene(_ scene: UIScene,
               willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {

        guard let windowScene = scene as? UIWindowScene else { return }
        windowScene.sizeRestrictions?.minimumSize.width = 500.0
    }
}
```

The example above specifies a preferred minimum width of 500 points.

> **Note**: The `UISceneSizeRestrictions` object does not prohibit other resizing behavior like rotation. When people rotate their device and the scene changes orientation, the scene’s bounds will change as well, regardless of the preferences expressed through the [`sizeRestrictions`](https://developer.apple.com/documentation/UIKit/UIWindowScene/sizeRestrictions) property of your app’s window scene. After the rotation has completed, the system will re-evaluate the size restrictions against the scene’s new bounds.

In SwiftUI, use the [`windowResizability(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/windowResizability(_:)) modifier to allow your scene’s content provide sizing information. The value that you specify indicates the strategy the system uses to place minimum restriction on windows that it creates from that scene. For example:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
               .frame(minWidth: 100, maxWidth: 400, minHeight: 100, maxHeight: 400)
        }
        .windowResizability(.contentMinSize)
    }
}
```

#### Request Scene Orientation Lock

Some apps may benefit from temporarily locking the orientation. For example, a driving game may want to lock the orientation when the device is expected to rotate for steering a vehicle or a camera apps may need to lock orientation during photo or video capture.

To request orientation lock, override [`prefersInterfaceOrientationLocked`](https://developer.apple.com/documentation/UIKit/UIViewController/prefersInterfaceOrientationLocked) in your view controller subclass. Whenever this preference changes, call [`setNeedsUpdateOfSupportedInterfaceOrientations()`](https://developer.apple.com/documentation/UIKit/UIViewController/setNeedsUpdateOfSupportedInterfaceOrientations()). For example:

```swift
class MyRaceViewController: UIViewController {

    override var prefersInterfaceOrientationLocked: Bool {
        return isDriving
    }

    // ...

    var isDriving: Bool = false {
        didSet {
            if isDriving != oldValue {
                setNeedsUpdateOfPrefersInterfaceOrientationLocked()
            }
        }
    }
}
```

The value returned by `prefersInterfaceOrientationLocked` indicates to the system that the view controller prefers the scene’s interface orientation to be locked when shown.

> **Note**: The system does not guarantee that `prefersInterfaceOrientationLocked` preference will be honored. If honored, the preference to lock the interface orientation lasts while the view controller is visible, or you call `setNeedsUpdateOfPrefersInterfaceOrientationLocked` again and return `false` as the value of `prefersInterfaceOrientationLocked`.

If your app uses the camera, use [`AVCaptureDevice.RotationCoordinator`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/RotationCoordinator) to ensure that captures and camera preview interfaces are correctly oriented regardless of interface orientation lock.

To observe the interface orientation lock, use `windowScene(_:didUpdateEffectiveGeometry:)` and check if the value of [`isInterfaceOrientationLocked`](https://developer.apple.com/documentation/UIKit/UIWindowScene/Geometry/isInterfaceOrientationLocked) has changed. For example:

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var game = MyGame()

    func windowScene(
        _ windowScene: UIWindowScene,
        didUpdateEffectiveGeometry previousGeometry: UIWindowScene.Geometry) {

        let wasLocked = previousGeometry.isInterfaceOrientationLocked
        let isLocked = windowScene.effectiveGeometry.isInterfaceOrientationLocked

        if wasLocked != isLocked {
            game.pauseIfNeeded(isInterfaceOrientationLocked: isLocked)
        }
    }
}
```

For more information about locking your scene to your preferred interface orientation and preventing rotation changes, see [`prefersInterfaceOrientationLocked`](https://developer.apple.com/documentation/UIKit/UIViewController/prefersInterfaceOrientationLocked).

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key)*