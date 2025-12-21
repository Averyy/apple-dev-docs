# TN3187: Migrating to the UIKit scene-based life cycle

**Framework**: Technotes

Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.

#### Overview

A scene represents an instance of your app’s user interface. In a document-based app, such as a text editor, each open document can be displayed in its own scene, enabling users to work on multiple documents side by side.

In iOS 18.4, iPadOS 18.4, Mac Catalyst 18.4, tvOS 18.4, visionOS 2.4 and later, UIKit logs the following message for apps that haven’t adopted the scene-based life-cycle:

```None
This process does not adopt UIScene lifecycle. 
This will become an assert in a future version.
```

In iOS 26, iPadOS 26, Mac Catalyst 26, tvOS 26, visionOS 26 , the log message has been updated to:

```None
UIScene lifecycle will soon be required. 
Failure to adopt will result in an assert in the future.
```

In the next major release following iOS 26, UIScene lifecycle will be required when building with the latest SDK; otherwise, your app won’t launch. While supporting multiple scenes is encouraged, only adoption of scene life-cycle is required.

This guide will help you add scene support to your app so you can receive scene-specific life-cycle events from UIKit and manage your user interface using scene objects and methods. For more information about how to configure scene support, see [`Specifying the scenes your app supports`](https://developer.apple.com/documentation/UIKit/specifying-the-scenes-your-app-supports).

#### Determine If Your App Should Migrate

Migrate to the scene-based life-cycle if your app meets either of the following conditions:

- The [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key is missing from your [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) or it has no specified configurations.
- You haven’t implemented the [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:)) method in your app delegate.

#### Understand the Scene Based Life Cycle

A scene contains the windows and view controllers for presenting one instance of your UI. UIKit manages each instance of your app’s UI using a [`UIWindowScene`](https://developer.apple.com/documentation/UIKit/UIWindowScene) object.

You can specify a [`UIWindowScene`](https://developer.apple.com/documentation/UIKit/UIWindowScene) object by including the class name for the scene in the `Info.plist` scene manifest.

Alternatively, you can specify the class name when creating a [`UISceneConfiguration`](https://developer.apple.com/documentation/UIKit/UISceneConfiguration) object in your app delegate’s `application(:configurationForConnecting:options:)` method. When the user interacts with your app, the system creates an appropriate scene object based on the configuration data you provided. To request a scene programmatically, call the [`activateSceneSession(for:errorHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/activateSceneSession(for:errorHandler:)) method of [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication).

In a scene-based app:

- UIKit usually creates a `UIWindowScene` object instead of a [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) object. When configuring your app’s scene support, specify `UIWindowScene` objects instead of `UIScene` objects.
- Use [`CPTemplateApplicationScene`](https://developer.apple.com/documentation/CarPlay/CPTemplateApplicationScene) if your app is adopting scenes for CarPlay. To learn how to add a CarPlay scene see [`Displaying Content in CarPlay`](https://developer.apple.com/documentation/CarPlay/displaying-content-in-carplay).
- [`UISceneSession`](https://developer.apple.com/documentation/UIKit/UISceneSession) contains a unique identifier and the configuration details of the scene.
- `UISceneDelegate` and [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate) both handle scene-specific life-cycle events.
- `UISceneConfiguration` defines how to create and configure scenes.

Unlike the `UIApplicationDelegate` object, which manages a single app-wide life-cycle, the scene-based life-cycle divides your app’s overall life cycle into two components:

- The application life cycle, such as when your app process launches.
- The life cycle of when an app has UI visible on screen, embodied by a scene.

#### Adopt the Scene Based Life Cycle

The simplest way to configure your app’s scenes is to add a `UIApplicationSceneManifest` key with a scene configuration in the `Info.plist` file.

Apps that require dynamic scene configurations, such as supporting multiple scenes, customizing scenes based on user activities, or handling different scene roles can implement the `application(_:configurationForConnecting:options:)` method in the app delegate.

##### Configure the Infoplist for Scene Support

To configure your `Info.plist` for scene support, you should add a `UIApplicationSceneManifest` key with a scene configuration:

1. Open your Xcode project.
2. Select your app target.
3. Navigate to the General settings for your app target.
4. Select “Scene manifest” in the Deployment Info section.
5. Edit the Info.plist file and add a `UIApplicationSceneManifest` key

For example:

```xml
<key>UIApplicationSceneManifest</key>
<dict>
    <key>UIApplicationSupportsMultipleScenes</key>
    <false/> 
    <key>UISceneConfigurations</key>
    <dict>
        <key>UIWindowSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneConfigurationName</key>
                <string>Default Configuration</string>
                <key>UISceneDelegateClassName</key>
                <string>$(PRODUCT_MODULE_NAME).SceneDelegate</string>
                <key>UISceneStoryboardFile</key>
                <string>Main</string> 
            </dict>
        </array>
    </dict>
</dict>
```

> **Note**: Supporting multiple scenes is optional. Adopting multiple scenes may require restructuring your app to make your data model more scene-specific. Consider whether your app’s user experience would benefit from it before supporting multiple scenes.

To support multiple scenes, include the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) key with its `Boolean` value set to `true`, which indicates that the app supports two or more scenes simultaneously. Each `UISceneConfiguration` should have a unique configuration name when supporting multiple scenes.

##### Provide Scene Configurations From Your App Delegate for Dynamic Configuration

Implement the `application(_:configurationForConnecting:options:)` method in your app delegate if you don’t include scene-configuration data in your app’s `Info.plist` file or if your app requires dynamic scene configuration—such as, loading different scenes based on user activity or session specific data.

```swift
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        configurationForConnecting connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {

        // Each UISceneConfiguration have a unique configuration name.
        // The configuration name is a app-specific name
        // you use to identify the scene, and it corresponds to entries
        // in the `Info.plist` scene manifest.
        var configurationName: String!
    
        switch options.userActivities.first?.activityType {
        case UserActivity.GalleryOpenInspectorActivityType:
            // Create a photo inspector window scene.
            configurationName = "Inspector Configuration"
        default:
            // Create a default gallery window scene.
            configurationName = "Default Configuration"
        }
        
        return UISceneConfiguration(
            name: configurationName,
            sessionRole: connectingSceneSession.role
        )
    }
}
```

In this example, through the use of a unique [`activityType`](https://developer.apple.com/documentation/Foundation/NSUserActivity/activityType), the app can distinguish which new scene to create.

To learn more about how to configure your app for different scene types and customize scene behavior, see [`Specifying the scenes your app supports`](https://developer.apple.com/documentation/UIKit/specifying-the-scenes-your-app-supports), and for more information about how to create multiple windows programmatically, see [`Supporting multiple windows on iPad`](https://developer.apple.com/documentation/UIKit/supporting-multiple-windows-on-ipad).

If your root view controller is loaded from the storyboard, ensure that the storyboard name is provided in the `UISceneConfigurations` key in the `Info.plist` scene manifest. The system automatically configures your window scene and its root view controller.

If your window’s root view controller is loaded programmatically, use [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) to create a `UIWindow` and associate it with the specified scene object.

```swift
import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    
    func scene(
        _ scene: UIScene,
        willConnectTo session: UISceneSession,
        options connectionOptions: UIScene.ConnectionOptions
    ) {
        // Confirm the scene is a window scene in iOS or iPadOS.
        guard let windowScene = scene as? UIWindowScene else { return }
                
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = YourRootViewController()
        window?.makeKeyAndVisible()
    }
}
```

This example uses a [`UIResponder`](https://developer.apple.com/documentation/UIKit/UIResponder) subclass conforming to the `UIWindowSceneDelegate` protocol called `SceneDelegate` to create the app’s primary window scene. For more information about how to prepare your app at launch time, see [`Responding to the launch of your app`](https://developer.apple.com/documentation/UIKit/responding-to-the-launch-of-your-app).

#### Migrate App Life Cycle Logic

Move your app’s existing life-cycle methods from `UIApplicationDelegate` to `UISceneDelegate`:

| UIApplicationDelegate | UISceneDelegate |
| --- | --- |
| [`applicationDidBecomeActive(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidBecomeActive(_:)) | [`sceneDidBecomeActive(_:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/sceneDidBecomeActive(_:)) |
| [`applicationWillResignActive(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillResignActive(_:)) | [`sceneWillResignActive(_:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/sceneWillResignActive(_:)) |
| [`applicationDidEnterBackground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidEnterBackground(_:)) | [`sceneDidEnterBackground(_:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/sceneDidEnterBackground(_:)) |
| [`applicationWillEnterForeground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillEnterForeground(_:)) | [`sceneWillEnterForeground(_:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/sceneWillEnterForeground(_:)) |

Migrating to a scene-based life-cycle modernizes your app and helps it to take full advantage of iOS multitasking features. After adopting scene-based life-cycle ensure to test your app in Split View, Slide Over, and Stage Manager on iPad.

To learn how to respond to state transitions within your app, see [`Managing your app’s life cycle`](https://developer.apple.com/documentation/UIKit/managing-your-app-s-life-cycle).

#### Revision History

-  Added information about the requirements in the major release following iOS 26.
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
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
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
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)*