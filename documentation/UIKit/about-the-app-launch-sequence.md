# About the app launch sequence

**Framework**: UIKit

Learn the order in which the system executes your code at app launch time.

#### Overview

An app launch involves a complex sequence of steps, most of which the system handles automatically. During the launch sequence, UIKit calls methods in your app delegate and scene delegate so you can prepare your app for user interaction and perform any tasks specific to your app’s requirements. The following illustrates the individual steps of this launch sequence, from when the user or system launches your app to when the sequence completes:

![A diagram that depicts an app’s launch sequence. On the left is a box with the title Launch time that contains a label for each step in the launch sequence, and a down arrow between each one that represents the direction of flow. From top-to-bottom, the labels are main(), UIApplicationMain, First app initialization, View controller state restoration, Final initialization, and Starts UI with connection to UIWindowScene + userActivity state restoration. On the right is a box with the title Your code that contains four labels. From top-to-bottom, the labels are application:willFinishLaunchingWithOptions:, Various methods, application:didFinishLaunchingWithOptions:, and scene:willConnectTo:options:. There is an arrow pointing right between the First app initialization label in the Launch time box and the application:willFinishLaunchingWithOptions: label in the Your code box. There’s a bidirectional arrow between the View controller state restoration label in the Launch time box and the Various methods label in the Your code box. There’s an arrow pointing right between the Final app initialization label in the Launch time box and the application:willFinishLaunchingWithOptions: label in the Your code box. And there’s an arrow from the Starts UI with connection to UIWindowScene + userActivity state restoration label in the Launch time box to the scene:willConnectTo:options: label in the Your code box.](https://docs-assets.developer.apple.com/published/2ccbb8e9d798da45630af11346f7930f/app-launch-sequence%402x.png)

1. The system executes the `main()` function that Xcode provides in an Objective-C project, or that’s available when you use `@main` in a Swift project.
2. The `main()` function calls [`UIApplicationMain(_:_:_:_:)`](uiapplicationmain(_:_:_:_:)-1yub7.md), which creates an instance of [`UIApplication`](uiapplication.md) and your app delegate.
3. UIKit calls the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) method in your app delegate.
4. UIKit performs view controller state restoration, which results in the execution of additional methods in your app delegate and app’s view controllers. For more information, see [`About the UI restoration process`](about-the-ui-restoration-process.md).
5. UIKit calls your app delegate’s [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method.
6. After the app launch completes, UIKit prepares a scene to connect to your app, and then calls [`scene(_:willConnectTo:options:)`](uiscenedelegate/scene(_:willconnectto:options:).md). UIKit may deliver a user activity to this method for you to handle during scene connection.

After the launch sequence completes, the system displays your app’s user interface and informs your app or scene delegates when life-cycle events occur.

##### Prepare Your App for Prewarming

In iOS 15 and later, the system may, depending on device conditions,  your app — launch nonrunning application processes to reduce the amount of time the user waits before the app is usable. Prewarming executes an app’s launch sequence up until, but not including, when `main()` calls [`UIApplicationMain(_:_:_:_:)`](uiapplicationmain(_:_:_:_:)-1yub7.md). This provides the system with an opportunity to build and cache any low-level structures it requires in anticipation of a full launch.

> **Note**:  For more information about the low-level structures the system requires during app launch, see the WWDC session video [`App Startup Time: Past, Present, and Future`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2017/413).

 For more information about the low-level structures the system requires during app launch, see the WWDC session video [`App Startup Time: Past, Present, and Future`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2017/413).

After the system prewarms your app, its launch sequence remains in a paused state until the app launches and the sequence resumes, or the system removes the prewarmed app from memory to reclaim resources. The system can prewarm your app after a device reboot, and periodically as system conditions allow.

If your app executes code before the call to [`UIApplicationMain(_:_:_:_:)`](uiapplicationmain(_:_:_:_:)-1yub7.md), such as in static initializers like [`load()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/load()), don’t make assumptions about what services and resources are available. For example, keychain items may be unavailable because their data protection policies require an unlocked device and prewarming happens even when the device is in a locked state. If your code is dependent upon access to a specific service or resource, migrate that code to a later part of the launch sequence.

Prewarming an app results in an indeterminate amount of time between when the prewarming phase completes and when the user, or system, fully launches the app. Because of this, use [`MetricKit`](https://developer.apple.com/documentation/MetricKit) to accurately measure user-driven launch and resume times instead of manually signposting various points of the launch sequence.

## See Also

- [Performing one-time setup for your app](performing-one-time-setup-for-your-app.md)
  Ensure proper configuration of your app environment.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-the-app-launch-sequence)*