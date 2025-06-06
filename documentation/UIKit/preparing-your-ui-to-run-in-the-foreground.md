# Preparing your UI to run in the foreground

**Framework**: UIKit

Configure your app to appear onscreen.

#### Overview

Use foreground transitions to prepare your app’s UI to appear onscreen. An app’s transition to the foreground is usually in response to a user action. For example, when the user taps the app’s icon, the system launches the app and brings it to the foreground. Use a foreground transition to update your app’s UI, acquire resources, and start the services you need to handle user requests.

All state transitions result in UIKit sending notifications to the appropriate delegate object:

- In iOS 13 and later — A [`UISceneDelegate`](uiscenedelegate.md) object.
- In iOS 12 and earlier — The [`UIApplicationDelegate`](uiapplicationdelegate.md) object.

You can support both types of delegate objects, but UIKit always uses scene delegate objects when they’re available. UIKit notifies only the scene delegate associated with the specific scene that’s entering the foreground. For information about how to configure scene support, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md).

##### Update Your Apps Data Model When Entering the Foreground

At launch time, the system starts your app in the inactive state before transitioning it to the foreground. Use your app’s launch-time methods to perform any work needed at that time. For an app that’s in the background, UIKit moves your app to the inactive state by calling one of the following methods:

- For apps that support scenes — The [`sceneWillEnterForeground(_:)`](uiscenedelegate/scenewillenterforeground(_:).md) method of the appropriate scene delegate object.
- For all other apps — The [`applicationWillEnterForeground(_:)`](uiapplicationdelegate/applicationwillenterforeground(_:).md) method.

When transitioning from the background to the foreground, use these methods to load resources from disk and fetch data from the network.

For information about how to prepare your app at launch time, see [`Responding to the launch of your app`](responding-to-the-launch-of-your-app.md).

##### Configure Your User Interface and Initial Tasks at Activation

The system moves your app to the active state immediately before displaying the app’s UI. Activation is a good time to configure your app’s UI and runtime behavior; specifically:

- Show your app’s windows, if needed.
- Change the currently visible view controller, if needed.
- Update the data values and state of views and controls.
- Display controls to resume a paused game.
- Start or resume any dispatch queues that you use to execute tasks.
- Update data source objects.
- Start timers for periodic tasks.

Put your configuration code in one of the following methods:

- For a scene-based UI — The [`sceneDidBecomeActive(_:)`](uiscenedelegate/scenedidbecomeactive(_:).md) method of the appropriate scene delegate object.
- For all other apps — The [`applicationDidBecomeActive(_:)`](uiapplicationdelegate/applicationdidbecomeactive(_:).md) method of your app delegate object.

Activation is also the time to put finishing touches on your UI before displaying it to the user. Don’t run any code that might block your activation method. Instead, make sure you have everything you need in advance. For example, if your data changes frequently outside of the app, use background tasks to fetch updates from the network before your app returns to the foreground. Otherwise, be prepared to display existing data while you fetch changes asynchronously.

##### Start Ui Specific Tasks When Your View Appears

When your activation method returns, UIKit shows any windows that you made visible. It also notifies any relevant view controllers that their views are about to appear. Use your view controller’s [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) method to perform any final updates to your interface. For example:

- Start user interface animations, as appropriate.
- Begin playing media files, if auto-play is enabled.
- Begin displaying graphics for games and immersive content at their full frame rates.

Don’t try to show a different view controller or make major changes to your user interface. By the time your view controller appears onscreen, your interface should be ready to display.

## Topics

### State-change notifications
- [Processing queued notifications](processing-queued-notifications.md)
  Respond to notifications when coming out of the suspended state.

## See Also

- [Preparing your UI to run in the background](preparing-your-ui-to-run-in-the-background.md)
  Prepare your app to be suspended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-foreground)*