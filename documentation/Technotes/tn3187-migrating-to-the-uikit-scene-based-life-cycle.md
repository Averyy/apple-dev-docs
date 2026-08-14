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

This guide will help you add scene support to your app so you can receive scene-specific life-cycle events from UIKit and manage your user interface using scene objects and methods. For more information about how to configure scene support, see [`Specifying the scenes your app supports`](https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports).

#### Determine If Your App Should Migrate

Migrate to the scene-based life-cycle if your app meets either of the following conditions:

- The [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest) key is missing from your [`Information Property List`](https://developer.apple.com/documentation/bundleresources/information-property-list) or it has no specified configurations.
- You haven’t implemented the [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:configurationforconnecting:options:)) method in your app delegate.

#### Understand the Scene Based Life Cycle

A scene contains the windows and view controllers for presenting one instance of your UI. UIKit manages each instance of your app’s UI using a [`UIWindowScene`](https://developer.apple.com/documentation/uikit/uiwindowscene) object.

You can specify a [`UIWindowScene`](https://developer.apple.com/documentation/uikit/uiwindowscene) object by including the class name for the scene in the `Info.plist` scene manifest.

Alternatively, you can specify the class name when creating a [`UISceneConfiguration`](https://developer.apple.com/documentation/uikit/uisceneconfiguration) object in your app delegate’s `application(:configurationForConnecting:options:)` method. When the user interacts with your app, the system creates an appropriate scene object based on the configuration data you provided. To request a scene programmatically, call the [`activateSceneSession(for:errorHandler:)`](https://developer.apple.com/documentation/uikit/uiapplication/activatescenesession(for:errorhandler:)) method of [`UIApplication`](https://developer.apple.com/documentation/uikit/uiapplication).

In a scene-based app:

- UIKit usually creates a `UIWindowScene` object instead of a [`UIScene`](https://developer.apple.com/documentation/uikit/uiscene) object. When configuring your app’s scene support, specify `UIWindowScene` objects instead of `UIScene` objects.
- Use [`CPTemplateApplicationScene`](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene) if your app is adopting scenes for CarPlay. To learn how to add a CarPlay scene see [`Displaying Content in CarPlay`](https://developer.apple.com/documentation/carplay/displaying-content-in-carplay).
- [`UISceneSession`](https://developer.apple.com/documentation/uikit/uiscenesession) contains a unique identifier and the configuration details of the scene.
- `UISceneDelegate` and [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate) both handle scene-specific life-cycle events.
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

To support multiple scenes, include the [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes) key with its `Boolean` value set to `true`, which indicates that the app supports two or more scenes simultaneously. Each `UISceneConfiguration` should have a unique configuration name when supporting multiple scenes.

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

In this example, through the use of a unique [`activityType`](https://developer.apple.com/documentation/foundation/nsuseractivity/activitytype), the app can distinguish which new scene to create.

To learn more about how to configure your app for different scene types and customize scene behavior, see [`Specifying the scenes your app supports`](https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports), and for more information about how to create multiple windows programmatically, see [`Supporting multiple windows on iPad`](https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad).

If your root view controller is loaded from the storyboard, ensure that the storyboard name is provided in the `UISceneConfigurations` key in the `Info.plist` scene manifest. The system automatically configures your window scene and its root view controller.

If your window’s root view controller is loaded programmatically, use [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:willconnectto:options:)) to create a `UIWindow` and associate it with the specified scene object.

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

This example uses a [`UIResponder`](https://developer.apple.com/documentation/uikit/uiresponder) subclass conforming to the `UIWindowSceneDelegate` protocol called `SceneDelegate` to create the app’s primary window scene. For more information about how to prepare your app at launch time, see [`Responding to the launch of your app`](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app).

#### Support External Display Scenes

When an [`external display`](https://developer.apple.comhttps://support.apple.com/guide/ipad/move-an-app-to-an-external-display-ipad8baf19a7/26/ipados/26) is connected and your app is running on the embedded display, the system may offer your app a scene with the [`windowExternalDisplayNonInteractive`](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive) role.

On [`compatible iPad models`](https://developer.apple.comhttps://support.apple.com/guide/ipad/aside/ipad3de50547/26/ipados/26) with extended display supported and enabled, the system presents your app’s scenes in windows on the external display. For iPhone and iPad models that don’t support extended displays, the system mirrors your app’s primary display on the external display.

If your app doesn’t present custom content on an external display, you don’t need to provide a scene configuration for the `windowExternalDisplayNonInteractive` role. The system continues to mirror your app’s primary display automatically. For example:

```swift
import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    
    func scene(
        _ scene: UIScene,
        willConnectTo session: UISceneSession,
        options connectionOptions: UIScene.ConnectionOptions
    ) {
        guard let windowScene = scene as? UIWindowScene else { return }
        
        if session.role == .windowApplication {
            window = UIWindow(windowScene: windowScene)
            window?.rootViewController = YourRootViewController()
            window?.makeKeyAndVisible()
        } else if session.role == .windowExternalDisplayNonInteractive {
            // Provide a window to present noninteractive content on the external display.
            // Otherwise, ignore this role to keep the mirroring behavior.
        }
    }
}
```

To present custom content on the external display, provide a scene configuration for the [`windowExternalDisplayNonInteractive`](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive) role and attach a [`UIWindow`](https://developer.apple.com/documentation/uikit/uiwindow) to the scene the system provides. When your app presents content for the `windowExternalDisplayNonInteractive` scene, it spans the full screen. Attaching a window to the external display scene disables screen mirroring. To restore the system’s default behavior, either extended display or screen mirroring, set the `windowScene` property of that [`UIWindow`](https://developer.apple.com/documentation/uikit/uiwindow) to `nil`. For example:

```swift
import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    var externalWindow: UIWindow?

    func scene(
        _ scene: UIScene,
        willConnectTo session: UISceneSession,
        options connectionOptions: UIScene.ConnectionOptions
    ) {
        guard let windowScene = scene as? UIWindowScene else { return }

        if session.role == .windowApplication {
            window = UIWindow(windowScene: windowScene)
            window?.rootViewController = YourRootViewController()
            window?.makeKeyAndVisible()
        } else if session.role == .windowExternalDisplayNonInteractive {
            externalWindow = UIWindow(windowScene: windowScene)
            externalWindow?.rootViewController = YourExternalDisplayViewController()
            externalWindow?.makeKeyAndVisible()
        }
    }

    // Stop presenting on the external display and restore the default behavior.
    func exitPhotoInspector() {
        externalWindow?.windowScene = nil
        externalWindow = nil
    }
}
```

If your app needs to override the system’s screen mirroring or present custom content on the external display, provide a scene configuration for the `windowExternalDisplayNonInteractive` role in either of the following ways:

- Add a [`UIWindowSceneSessionRoleExternalDisplayNonInteractive`](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleexternaldisplaynoninteractive) entry to `UISceneConfiguration` in your `Info.plist` file.
- Inspect [`UISceneSession.Role`](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct) in [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:configurationforconnecting:options:)) and return a `UISceneConfiguration` configured for the `windowExternalDisplayNonInteractive` role.

For more information about presenting content on connected displays, see [`Presenting content on a connected display`](https://developer.apple.com/documentation/uikit/presenting-content-on-a-connected-display).

#### Migrate App Life Cycle Logic

Move your app’s existing life-cycle methods from `UIApplicationDelegate` to `UISceneDelegate`:

| UIApplicationDelegate | UISceneDelegate |
| --- | --- |
| [`applicationDidBecomeActive(_:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidbecomeactive(_:)) | [`sceneDidBecomeActive(_:)`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenedidbecomeactive(_:)) |
| [`applicationWillResignActive(_:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillresignactive(_:)) | [`sceneWillResignActive(_:)`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenewillresignactive(_:)) |
| [`applicationDidEnterBackground(_:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidenterbackground(_:)) | [`sceneDidEnterBackground(_:)`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenedidenterbackground(_:)) |
| [`applicationWillEnterForeground(_:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationwillenterforeground(_:)) | [`sceneWillEnterForeground(_:)`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scenewillenterforeground(_:)) |

Migrating to a scene-based life-cycle modernizes your app and helps it to take full advantage of iOS multitasking features. After adopting scene-based life-cycle ensure to test your app in Split View, Slide Over, and Stage Manager on iPad.

To learn how to respond to state transitions within your app, see [`Managing your app’s life cycle`](https://developer.apple.com/documentation/uikit/managing-your-app-s-life-cycle).

#### Revision History

- **2026-03-16** Added information about supporting external display scenes.
- **2025-06-23** Added information about the requirements in the major release following iOS 26.
- **2025-05-05** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)*