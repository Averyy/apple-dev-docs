# Transitioning to the UIKit scene-based life cycle

**Framework**: UIKit

Adopt the scene-based life cycle to replace the app delegate life cycle in UIKit.

#### Overview

The UIKit scene-based life cycle separates the app process life cycle from the UI life cycle, allowing apps to manage multiple instances of UI independently. For example, a document-based app, such as a text editor, can display each open document in its own scene, letting people work on multiple documents side by side. Your app process launches once and [`UIApplicationDelegate`](uiapplicationdelegate.md) handles it, but each piece of visible UI — each *scene* — has its own independent life cycle that [`UISceneDelegate`](uiscenedelegate.md) and [`UIWindowSceneDelegate`](uiwindowscenedelegate.md) coordinate. [`UISceneDelegate`](uiscenedelegate.md) handles basic life-cycle events that apply to all scenes, while [`UIWindowSceneDelegate`](uiwindowscenedelegate.md) takes care of UI-specific events like window controls and geometry changes. A scene can go to the background while another stays active, and the system can create, destroy, and arrange scenes without affecting others.

UIKit represents each scene as a [`UIWindowScene`](uiwindowscene.md) object. For your app’s code, this means life-cycle events no longer occur globally — they occur per scene. Tasks like saving state or updating your UI happen at the scene level rather than the app level.

> ❗ **Important**:  Adopting the scene-based life cycle is required. Beginning in iOS 27, iPadOS 27, Mac Catalyst 27, tvOS 27, and visionOS 27, apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch.

For more information about configuring scene support, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md).

Starting in iOS 18.4, iPadOS 18.4, Mac Catalyst 18.4, tvOS 18.4, and visionOS 2.4, UIKit logs this message for apps that haven’t migrated:

```other
This process does not adopt UIScene lifecycle. 
This will become an assert in a future version.
```

In iOS 26, iPadOS 26, Mac Catalyst 26, tvOS 26, and visionOS 26, the message changes to:

```other
UIScene lifecycle will soon be required.
Failure to adopt will result in an assert in the future.
```

#### Determine If Your App Needs to Migrate

Migrate to the scene-based life cycle if your app meets either of the following conditions:

- The [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key is missing from your information property list, or it has no specified configurations.
- Your app delegate doesn’t implement [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md).

#### Adopt the Scene Based Life Cycle

To configure your app’s scenes, add a [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key with a scene configuration to your information property list. If your app requires dynamic scene configurations — such as customizing scenes based on user activities, or handling different scene roles — implement [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) in your app delegate instead.

##### Configure the Information Property List for Scene Support

Add a [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key with a scene configuration to your information property list:

1. Open your Xcode project.
2. Select your app target.
3. Go to the General settings for your app target.
4. Select “Scene manifest” in the Deployment Info section.
5. Add a [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest) key to the information property list.

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

> **Note**: Supporting multiple scenes is optional, and may require restructuring your app’s data model to be scene-specific. Consider whether your app’s user experience benefits from multiple scenes before enabling it. To support multiple scenes, set [`UIApplicationSupportsMultipleScenes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsMultipleScenes) to `true` and give each [`UISceneConfiguration`](uisceneconfiguration.md) a unique configuration name.

##### Provide Scene Configurations From Your App Delegate

Implement [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) in your app delegate if your app doesn’t include scene-configuration data in its information property list, or if it requires dynamic scene configuration — such as loading different scenes based on session-specific data:

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        configurationForConnecting connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {

        // Each `UISceneConfiguration` must have a unique configuration name
        // that corresponds to an entry in the information property list scene manifest.
        let configurationName: String

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

In this example, the app uses the [`activityType`](https://developer.apple.com/documentation/Foundation/NSUserActivity/activityType) property to determine which scene to create. For more information about configuring your app for different scene types, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md). For information about creating multiple windows programmatically, see [`Supporting multiple windows on iPad`](supporting-multiple-windows-on-ipad.md).

##### Configure Your Window Scene

UIKit creates a [`UIWindowScene`](uiwindowscene.md) object for each scene instance. When configuring scene support, specify `UIWindowScene` objects rather than [`UIScene`](uiscene.md) objects. If your app adopts scenes for CarPlay, use [`CPTemplateApplicationScene`](https://developer.apple.com/documentation/CarPlay/CPTemplateApplicationScene) instead. To learn how to add a CarPlay scene, see [`Displaying Content in CarPlay`](https://developer.apple.com/documentation/CarPlay/displaying-content-in-carplay).

If you load your root view controller from the storyboard, include the storyboard name in the [`UISceneConfigurations`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UISceneConfigurations) key in your information property list scene manifest. The system automatically configures your window scene and root view controller.

If you load your root view controller programmatically, implement [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md) to create a [`UIWindow`](uiwindow.md) and associate it with the scene:

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

        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = YourRootViewController()
        window?.makeKeyAndVisible()
    }
}
```

`SceneDelegate` is a [`UIResponder`](uiresponder.md) subclass that conforms to [`UIWindowSceneDelegate`](uiwindowscenedelegate.md). For more information about preparing your app at launch time, see [`Responding to the launch of your app`](responding-to-the-launch-of-your-app.md).

#### Migrate App Life Cycle Logic

Move your app’s existing life-cycle methods from [`UIApplicationDelegate`](uiapplicationdelegate.md) to [`UISceneDelegate`](uiscenedelegate.md):

| UIApplicationDelegate | UISceneDelegate |
| --- | --- |
| [`applicationDidBecomeActive(_:)`](uiapplicationdelegate/applicationdidbecomeactive(_:).md) | [`sceneDidBecomeActive(_:)`](uiscenedelegate/scenedidbecomeactive(_:).md) |
| [`applicationWillResignActive(_:)`](uiapplicationdelegate/applicationwillresignactive(_:).md) | [`sceneWillResignActive(_:)`](uiscenedelegate/scenewillresignactive(_:).md) |
| [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) | [`sceneDidEnterBackground(_:)`](uiscenedelegate/scenedidenterbackground(_:).md) |
| [`applicationWillEnterForeground(_:)`](uiapplicationdelegate/applicationwillenterforeground(_:).md) | [`sceneWillEnterForeground(_:)`](uiscenedelegate/scenewillenterforeground(_:).md) |

After migrating, test your app in Full Screen Apps, Windowed Apps, and Stage Manager on iPad. To learn how to respond to state transitions, see [`Managing your app’s life cycle`](managing-your-app-s-life-cycle.md).

#### Support Noninteractive External Display Scenes

If your app doesn’t present custom content on an external display, you don’t need to configure anything for this scene role. When an external display connects, the system mirrors your app’s primary display, or, on compatible iPad models with extended display enabled, presents your app’s interactive windows on the external display.

In iOS 26 and earlier, the system connected a [`windowExternalDisplayNonInteractive`](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) scene automatically, and your app opted out by declining to provide content for it. Beginning in iOS 27, your app receives this scene only after it registers a *scene accessory*. A scene accessory declares supplementary content that the system presents on your app’s behalf when associated functionality becomes available, such as an external display connected by cable or AirPlay. Your app declares what content to provide, and the system decides when and where to present it. Because the content appears only when a display is available, design your app to remain fully functional without the external display.

If your app previously provided content for this scene by checking the connecting scene’s role in [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) or your scene delegate, remove that role-specific logic and register a scene accessory instead. You can reuse your existing scene delegate as the accessory’s delegate class, or create a new one dedicated to the external-display scene.

Register the accessory on a view controller in your app’s main interface. Choose the view controller whose content the external display supplements:

```swift
class PlayerViewController: UIViewController {
    var displayRegistration: UISceneAccessoryRegistration?

    override func viewDidLoad() {
        super.viewDidLoad()

        // Describe the scene to present, including the delegate that attaches its window.
        let configuration = UISceneConfiguration()
        configuration.delegateClass = ExternalDisplaySceneDelegate.self

        // Register the accessory so the system can present this content on an external display.
        let accessory = UISceneAccessory.externalNonInteractive(sceneConfiguration: configuration)
        displayRegistration = registerSceneAccessory(accessory)
    }
}
```

While your app presents the view controller and an external display is available, the system connects the scene and calls [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md) on your delegate. Content for this scene spans the full screen.

For more information about presenting content on connected displays, including how to control when your content appears, respond to display availability, and stop presenting content, see [`Presenting content on a connected display`](presenting-content-on-a-connected-display.md).

## See Also

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md)
  Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.
- [class UIApplication](uiapplication.md)
  The centralized point of control and coordination for apps running in iOS.
- [protocol UIApplicationDelegate](uiapplicationdelegate.md)
  A set of methods to manage shared behaviors for your app.
- [Scenes](scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle)*