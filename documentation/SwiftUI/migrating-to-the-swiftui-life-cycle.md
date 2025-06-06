# Migrating to the SwiftUI life cycle

**Framework**: SwiftUI

Use a scene-based life cycle in SwiftUI while keeping your existing codebase.

#### Overview

Take advantage of the declarative syntax in SwiftUI and its compatibility with spatial frameworks by moving your app to the SwiftUI life cycle.

Moving to the SwiftUI life cycle requires several steps, including changing your app’s entry point, configuring the launch of your app, and monitoring life-cycle changes with the methods that SwiftUI provides.

##### Change Your Apps Entry Point

The [`UIKit`](https://developer.apple.com/documentation/UIKit) framework defines the `AppDelegate` file as the entry point of your app with the annotation `@main`. For more information on `@main`, see the [`Attributes`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#main) section in The Swift Programming Language. To indicate the entry of a SwiftUI app, you’ll need to create a new file that defines your app’s structure.

1. Open your project in Xcode.
2. Choose File > New > File > Swift file.
3. Name the file `<YourAppName>App.swift`.
4. Add `import SwiftUI` at the top of the file.
5. Annotate the app structure with the `@main` attribute to indicate the entry point of the SwiftUI app, as shown in the code snippet below.

> ❗ **Important**: Remove the `@main` or `@UIApplicationMain` attribute in your app delegate.

Remove the `@main` or `@UIApplicationMain` attribute in your app delegate.

Use following code to create the SwiftUI app structure. To learn more about this structure, follow the tutorial in [`Exploring the structure of a SwiftUI app`](https://developer.apple.comhttps://developer.apple.com/tutorials/swiftui-concepts/exploring-the-structure-of-a-swiftui-app).

```swift
import SwiftUI

@main
struct MyExampleApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

##### Support App Delegate Methods

To continue using methods in your app delegate, use the [`UIApplicationDelegateAdaptor`](uiapplicationdelegateadaptor.md) property wrapper. To tell SwiftUI about a delegate that conforms to the [`UIApplicationDelegate`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate) protocol, place this property wrapper inside your [`App`](app.md) declaration:

```swift
@main
struct MyExampleApp: App {
    @UIApplicationDelegateAdaptor private var appDelegate: MyAppDelegate
    var body: some Scene { ... }
}
```

This example marks a custom app delegate named `MyAppDelegate` as the delegate adaptor. Be sure to implement any necessary delegate methods in that type.

> **Note**: For AppKit support, use [`NSApplicationDelegateAdaptor`](nsapplicationdelegateadaptor.md). For WatchKit support, use [`WKApplicationDelegateAdaptor`](wkapplicationdelegateadaptor.md).

For AppKit support, use [`NSApplicationDelegateAdaptor`](nsapplicationdelegateadaptor.md). For WatchKit support, use [`WKApplicationDelegateAdaptor`](wkapplicationdelegateadaptor.md).

##### Configure the Launch of Your App

If you’re migrating an app that contains storyboards to SwiftUI, make sure to remove them when they’re no longer needed.

1. Open your project in Xcode.
2. Remove `Main.storyboard` from the project navigator.
3. Choose your app’s target.
4. Open the `Info.plist` file.
5. Remove the [`UIMainStoryboardFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIMainStoryboardFile) key.
6. Remove the [`UISceneStoryboardFile`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication/UISceneStoryboardFile) key in the [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) > [`UISceneConfigurations`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations) > [`UIWindowSceneSessionRoleApplication`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations/UIWindowSceneSessionRoleApplication) > `Item 0 (Default Configuration)` dictionary.

This figure shows the structure of the `Info.plist` file before removing these keys.

![A screenshot of the Info.plist file in Xcode, with all of the keys expanded.](https://docs-assets.developer.apple.com/published/4e9649de38316b3d418b3be2dcf02132/Migrating-to-the-SwiftUI-life-cycle-info_plist%402x.png)

The scene delegate continues to be called after removing the keys from the `Info.plist` file, so you can still handle other scene-based life cycle changes in this file. If you were previously launching your app in your scene delegate, remove the [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) method from your scene delegate.

If you didn’t previously support scenes in your app and rely on your app delegate to respond to the launch of your app, ensure you’re no longer setting a root view controller in [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)). Instead, return `true`.

##### Monitor Life Cycle Changes

You will no longer be able to monitor life-cycle changes in your app delegate due to the scene-based nature of SwiftUI (see [`Scene`](scene.md)). Prefer to handle these changes in [`ScenePhase`](scenephase.md), the life cycle enumeration that SwiftUI provides to monitor the phases of a scene. Observe the [`Environment`](environment.md) value to initiate actions when the phase changes.

```swift
@Environment(\.scenePhase) private var scenePhase
```

Interpret the value differently based on where you read it from. If you read the phase from inside a [`View`](view.md) instance, the value reflects the phase of the scene that contains the view. If you read the phase from within an `App` instance, the value reflects an aggregation of the phases of all of the scenes in your app.

To handle scene-based events with a scene delegate, provide your scene delegate to your SwiftUI app inside your app delegate. For more information, see the “Scene delegates” section of [`UIApplicationDelegateAdaptor`](uiapplicationdelegateadaptor.md).

For more information on handling scene-based life cycle events, see [`Managing your app’s life cycle`](https://developer.apple.com/documentation/UIKit/managing-your-app-s-life-cycle).

## See Also

- [Destination Video](../visionOS/destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Backyard Birds: Building an app with SwiftData and widgets](backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
- [Food Truck: Building a SwiftUI multiplatform app](food_truck_building_a_swiftui_multiplatform_app.md)
  Create a single codebase and app target for Mac, iPad, and iPhone.
- [Fruta: Building a Feature-Rich App with SwiftUI](../appclip/fruta_building_a_feature-rich_app_with_swiftui.md)
  Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [protocol App](app.md)
  A type that represents the structure and behavior of an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/migrating-to-the-swiftui-life-cycle)*