# Responding to the launch of your app

**Framework**: UIKit

Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.

#### Overview

The system launches your app when the user taps your app’s icon on the Home Screen. If your app requested specific events, the system might also launch your app in the background to handle those events.

All apps have an associated process and at least one scene, which the [`UIApplication`](uiapplication.md) and [`UIScene`](uiscene.md) objects represent. Apps also have an  — an object that conforms to the [`UIApplicationDelegate`](uiapplicationdelegate.md) protocol — which responds to important events happening within that process. Even an app that implements the scene life cycle uses an app delegate to manage fundamental events like launch and termination. At launch time, UIKit automatically creates the [`UIApplication`](uiapplication.md) object and your app delegate. It then starts your app’s main event loop before connecting to one or more of your app’s scenes.

##### Provide a Launch Storyboard

When the user first launches your app on a device, the system displays your launch storyboard until your app is ready to display its UI. Displaying the launch storyboard assures the user that your app launched and is doing something. If your app initializes itself and readies its UI quickly, the user may see your launch storyboard only briefly.

Xcode projects automatically include a default launch storyboard for you to customize, and you can add more launch storyboards as necessary. To add new launch storyboards to your project, do the following:

1. Open your project in Xcode.
2. Choose File > New > File.
3. Add a Launch Screen resource to your project.

Add views to your launch storyboard and use Auto Layout constraints to size and position them so that they adapt to the underlying environment. UIKit displays exactly what you provide, using your constraints to fit your views into the available space. For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/launching/).

> ❗ **Important**:  Don’t use a static image for your launch screen. In iOS 14 and later, the launch screen is limited to 25 MB.

##### Initialize Your Apps Data Structures

Put your app’s launch-time initialization code in one or both of the following methods:

- [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md)
- [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)

UIKit calls these methods at the beginning of your app’s launch cycle. Use them to:

- Initialize data structures that your app uses across scenes.
- Verify that your app has the resources it needs to run.
- Perform any one-time setup when your app launches for the first time. For example, install templates or user-modifiable files in a writable directory. See [`Performing one-time setup for your app`](performing-one-time-setup-for-your-app.md).
- Connect to any critical services that your app uses. For example, connect to the Apple Push Notification service if your app supports remote notifications.
- Check the launch options dictionary for information about why your app launched. See [`Determine why your app launched`](responding-to-the-launch-of-your-app#Determine-why-your-app-launched.md).

For apps that haven’t adopted the scene life cycle, UIKit loads your default user interface automatically at launch time. Use the [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method to make additional changes to that interface before it appears onscreen. For example, you might install a different view controller to reflect what the user was doing the last time they used the app.

##### Move Long Running Tasks Off the Main Thread

When the user launches your app, make a good impression by launching quickly. Performing long-running tasks in [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md), [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md), or [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md) might make your app appear sluggish to the user. Returning quickly is also important when launching to the background because the system limits your app’s background execution time.

Move tasks that aren’t critical to your app’s initialization out of the launch-time sequence. For example:

- Defer the initialization of features that your app doesn’t need immediately.
- Move important, long-running tasks off your app’s main thread. For example, run them asynchronously on a global dispatch queue or in a [`Task`](https://developer.apple.com/documentation/Swift/Task).

##### Determine Why Your Scene Connected

When UIKit connects to a scene in your app, it passes along a [`UIScene.ConnectionOptions`](uiscene/connectionoptions.md) object that contains information about why UIKit connected to the scene. For example, this could indicate that the user requested your app to open a [`URL`](https://developer.apple.com/documentation/Foundation/URL), which you might use to display a screen related to information provided in the `URL`.

The following code shows how you can check for a `URL` that contains information in query items in the scene’s connection options:

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        
        // Confirm the scene is a window scene in iOS or iPadOS. 
        guard let _ = (scene as? UIWindowScene) else { return }
        
        // Check if the scene connection options include a URL,
        // and whether the URL has query items.
        guard let linkedUrl = connectionOptions.urlContexts.first?.url,
              let linkedComponents = URLComponents(url: linkedUrl, resolvingAgainstBaseURL: false),
              let queryItems = linkedComponents.queryItems,
              !queryItems.isEmpty else {
            return
        }
        
        // Check and handle the URL and query items here.
    }
    // other methods…
}
```

##### Determine Why Your App Launched

When UIKit launches your app, it calls the  [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods to indicate when it’s reached these points in your app’s launch process. If your app hasn’t implemented the scene life cycle, UIKit passes along a launch options dictionary to these methods with information about why your app launched. The keys in that dictionary indicate important tasks to perform immediately. For example, they might reflect actions that the user started elsewhere and wants to continue in your app. Always check the contents of the launch options dictionary for keys that you expect, and respond appropriately to their presence.

> ❗ **Important**: When you adopt the scene life cycle, UIKit calls the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods, but no longer provides the launch options dictionary to those methods. Implement the scene connection methods instead to receive details about your app launch and scene connection. For more information, see [`Scenes`](scenes.md).

The following code shows the app delegate method for an app that handles receiving a `URL`. The code checks the launch options for an incoming URL, and whether that `URL` contains query items that you can use to configure your app. If not, the code returns `false` to indicate that your app can’t handle the launch options.

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        
        // Check if the launch options include a URL,
        // and whether the URL has query items.
        guard let linkedUrl = launchOptions?[.url] as? URL,
              let linkedComponents = URLComponents(url: linkedUrl, resolvingAgainstBaseURL: false),
              let queryItems = linkedComponents.queryItems,
              !queryItems.isEmpty else {
            return false
        }
        
        // Check whether your app can handle the URL and query
        // items here. Then return `true` if so, otherwise `false`.
        // ...
        
        return true
    }
    // other methods…
}
```

The system doesn’t include a key unless your app supports the corresponding feature. For example, the system doesn’t include the [`remoteNotification`](uiapplication/launchoptionskey/remotenotification.md) key for an app that doesn’t support remote notifications.

For a list of launch option keys and information about how to handle them, see [`UIApplication.LaunchOptionsKey`](uiapplication/launchoptionskey.md).

## Topics

### Launch time
- [About the app launch sequence](about-the-app-launch-sequence.md)
  Learn the order in which the system executes your code at app launch time.
- [Performing one-time setup for your app](performing-one-time-setup-for-your-app.md)
  Ensure proper configuration of your app environment.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.

## See Also

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [class UIApplication](uiapplication.md)
  The centralized point of control and coordination for apps running in iOS.
- [protocol UIApplicationDelegate](uiapplicationdelegate.md)
  A set of methods to manage shared behaviors for your app.
- [Scenes](scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app)*