# About the app launch sequence

**Framework**: UIKit

Learn the order in which the system executes your code at app launch time.

#### Overview

An app launch involves a complex sequence of steps, most of which the system handles automatically. During the launch sequence, UIKit calls methods in your app delegate and scene delegate so you can prepare your app for user interaction and perform any tasks specific to your app’s requirements. The following illustrates the individual steps of this launch sequence, from when the user or system launches your app to when the sequence completes:

![A diagram that depicts an app’s launch sequence. On the left is a box with the title Launch time that contains a label for each step in the launch sequence, and a down arrow between each one that represents the direction of flow. From top-to-bottom, the labels are main(), UIApplicationMain, First app initialization, View controller state restoration, Final app initialization, and Starts UI with connection to UIWindowScene + userActivity state restoration. On the right is a box with the title Your code that contains four labels. From top-to-bottom, the labels are application:willFinishLaunchingWithOptions:, Various methods, application:didFinishLaunchingWithOptions:, and scene:willConnectTo:options:. There is an arrow pointing right between the First app initialization label in the Launch time box and the application:willFinishLaunchingWithOptions: label in the Your code box. There’s a bidirectional arrow between the View controller state restoration label in the Launch time box and the Various methods label in the Your code box. There’s an arrow pointing right between the Final app initialization label in the Launch time box and the application:willFinishLaunchingWithOptions: label in the Your code box. And there’s an arrow from the Starts UI with connection to UIWindowScene + userActivity state restoration label in the Launch time box to the scene:willConnectTo:options: label in the Your code box.](/images/com.apple.uikit/app-launch-sequence@2x.png)

1. The system executes the `main()` function that Xcode provides in an Objective-C project, or that’s available when you use `@main` in a Swift project.
2. The `main()` function calls [`UIApplicationMain(_:_:_:_:)`](uiapplicationmain(_:_:_:_:)-1yub7.md), which creates an instance of [`UIApplication`](uiapplication.md) and your app delegate.
3. UIKit calls the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) method in your app delegate.
4. UIKit performs view controller state restoration, which calls additional methods in your app delegate and view controllers. For more information, see [`About the UI restoration process`](about-the-ui-restoration-process.md).
5. UIKit calls your app delegate’s [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method.
6. After the app launch completes, UIKit prepares a scene to connect to your app, and then calls [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md). UIKit may deliver a user activity to this method for you to handle during scene connection.

After the launch sequence completes, the system displays your app’s user interface and informs your app or scene delegates when life-cycle events occur.

Depending on device conditions, the system may *prewarm* your app — launch nonrunning app processes to reduce the amount of time a person waits before the app is usable. Prewarming creates your process and loads the libraries your app links against, then suspends your process without allowing any application code to run.

After the system prewarms your app’s process, that new process remains in a suspended state until the system wakes your app to continue into the standard launch sequence, or the system ends the prewarmed process to reclaim resources. The system can prewarm your app after a device reboot, and periodically as system conditions allow.

##### Optimize App Launch Performance

To achieve faster startup times, minimize the amount of work your app performs before the call to [`UIApplicationMain(_:_:_:_:)`](uiapplicationmain(_:_:_:_:)-1yub7.md). Running expensive or time-consuming code in methods that the system calls automatically before `main()`, such as [`load()`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/load()), can slow down your app’s launch time.

Consider deferring complex initialization tasks to later in the launch sequence. For UI-level tasks — such as configuring your interface or responding to a user activity — defer work to your scene delegate’s [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md), [`sceneWillEnterForeground(_:)`](uiscenedelegate/scenewillenterforeground(_:).md), or [`sceneDidBecomeActive(_:)`](uiscenedelegate/scenedidbecomeactive(_:).md) methods. For tasks that aren’t specific to a scene, such as setting up a database layer or configuring app-wide services, use your app delegate’s [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) or [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods. This approach improves launch performance and ensures that initialization occurs when your app has full access to system services.

Use [`MetricKit`](https://developer.apple.com/documentation/metrickit) to accurately measure user-driven launch and resume times and identify opportunities for optimization.

## See Also

- [Performing one-time setup for your app](performing-one-time-setup-for-your-app.md)
  Ensure proper configuration of your app environment.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-the-app-launch-sequence)*