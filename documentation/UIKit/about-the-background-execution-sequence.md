# About the background execution sequence

**Framework**: UIKit

Learn the order in which your custom code is executed when your app moves to the background.

#### Overview

An app may enter the background from one of several different starting points. System events can cause a suspended app to be returned to the background, or cause a not running app to be launched directly into the background. A foreground app transitions to the background when another app is launched or when the user returns to the Home screen.

![An app may launch into the background or transition from the foreground to the background. When it finishes processing events in the background, the system takes a snapshot of the app’s UI before moving it to the suspended state.](https://docs-assets.developer.apple.com/published/ca60d404bad2ea27f8d50a1902aa4f88/media-3004365%402x.png)

##### Handle Background Events

For apps that support one of the Background Modes capabilities, the system launches or resumes the app in the background to handle events associated with those capabilities. For example, the system might launch or resume the app to respond to a location update or to perform a background fetch.

![Apps may enable multiple background modes, and be launched in response to events for any of them.](https://docs-assets.developer.apple.com/published/5f72a1ec636590afd814bd920a576e4a/media-3004375%402x.png)

If your app isn’t running when an event arrives, the system launches the app and moves it directly to the background, following this sequence:

1. The system launches the app and follows the initialization sequence described in [`About the app launch sequence`](about-the-app-launch-sequence.md).
2. UIKit calls the app delegate’s [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method.
3. UIKit delivers the event that caused the launch.
4. The app’s snapshot is taken.
5. The app may be suspended again.

If your app is in memory and suspended when an event arrives, the system resumes the app in the background, following this sequence:

1. The system resumes the app.
2. UIKit calls the app delegate’s [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method.
3. UIKit delivers the event that caused the launch.
4. The app’s snapshot is taken.
5. The app may be suspended again.

##### Transition From the Foreground

When another app is launched or the user returns to the Home screen, the foreground app moves to the background, following this sequence:

1. The user exits the running app.
2. UIKit calls the app delegate’s [`applicationWillResignActive(_:)`](uiapplicationdelegate/applicationwillresignactive(_:).md) method.
3. UIKit calls the app delegate’s [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method.
4. The app’s snapshot is taken.
5. The app may be suspended again.

## See Also

- [Using background tasks to update your app](using-background-tasks-to-update-your-app.md)
  Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [Extending your app’s background execution time](extending-your-app-s-background-execution-time.md)
  Ensure that critical tasks finish when your app moves to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/about-the-background-execution-sequence)*