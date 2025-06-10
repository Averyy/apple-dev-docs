# Preparing your UI to run in the background

**Framework**: UIKit

Prepare your app to be suspended.

#### Overview

Apps move to the background state for many reasons. When the user exits a foreground app, that app moves to the background state briefly before UIKit suspends it. The system may also launch an app directly into the background state, or move a suspended app into the background, and give it time to perform important tasks.

When your app is in the background, it should do as little as possible, and preferably nothing. If your app was previously in the foreground, use the background transition to stop tasks and release any shared resources. If your app enters the background to process an important event, process the event and exit as quickly as possible.

All state transitions result in UIKit sending notifications to the appropriate delegate object:

- In iOS 13 and later — A [`UISceneDelegate`](uiscenedelegate.md) object.
- In iOS 12 and earlier — The [`UIApplicationDelegate`](uiapplicationdelegate.md) object.

You can support both types of delegate objects, but UIKit always uses scene delegate objects when they’re available. UIKit notifies only the scene delegate associated with the specific scene that’s entering the background.

##### Quiet Your App Upon Deactivation

The system deactivates apps for several reasons. When the user exits the foreground app, the system deactivates that app immediately before moving it to the background. The system also deactivates apps when it needs to interrupt them temporarily — for example, to display system alerts. In the case of a system panel, the system reactivates the app when the user dismisses the panel.

During deactivation, UIKit calls one of the following methods of your app:

- For apps that support scenes — The [`sceneWillResignActive(_:)`](uiscenedelegate/scenewillresignactive(_:).md) method of the appropriate scene delegate object.
- For all other apps — The [`applicationWillResignActive(_:)`](uiapplicationdelegate/applicationwillresignactive(_:).md) method of the app delegate object.

Use deactivation to preserve the user’s data and put your app in a quiet state by pausing all major work; specifically:

- Save user data to disk and close any open files.
- Suspend dispatch and operation queues.
- Don’t schedule any new tasks for execution.
- Invalidate any active timers.
- Pause gameplay automatically.
- Don’t commit any new Metal work to be processed.
- Don’t commit any new OpenGL commands.

##### Release Resources Upon Entering the Background

When your app transitions to the background, release memory and free up any shared resources your app is holding. For an app transitioning from the foreground to the background, freeing up memory is especially important. The foreground has priority over memory and other system resources, and the system terminates background apps as needed to make those resources available. Even if your app wasn’t in the foreground, perform checks to ensure that it consumes as few resources as possible.

Upon entering the background, UIKit calls one of the following methods of your app:

- For apps that support scenes — The [`sceneDidEnterBackground(_:)`](uiscenedelegate/scenedidenterbackground(_:).md) method of the appropriate scene delegate object.
- For all other apps — The [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method of the app delegate object.

During a background transition, perform as many of the following tasks as makes sense for your app:

- Discard any images or media that you read directly from files.
- Discard any large, in-memory objects that you can recreate or reload from disk.
- Release access to the camera and other shared hardware resources.
- Hide sensitive information (such as passwords) in your app’s user interface.
- Dismiss alerts and other temporary interfaces.
- Close connections to any shared system databases.
- Unregister from Bonjour services and close any listening sockets associated with them.
- Ensure that all Metal command buffers have been scheduled. For more information, see [`Preparing Your Metal App to Run in the Background`](https://developer.apple.com/documentation/Metal/preparing-your-metal-app-to-run-in-the-background).
- Ensure that all OpenGL commands you previously submitted have finished.

You don’t need to discard named images that you loaded from your app’s asset catalog. Similarly, you don’t need to release objects that adopt the [`NSDiscardableContent`](https://developer.apple.com/documentation/Foundation/NSDiscardableContent) protocol or that you manage using an [`NSCache`](https://developer.apple.com/documentation/Foundation/NSCache) object. The system automatically handles the cleanup of those objects.

Make sure your app isn’t holding any shared system resources when it transitions to the background. If it continues accessing resources like the camera or a shared system database after transitioning to the background, the system terminates your app to free up that resource. If you use a system framework to access a resource, check the framework’s documentation for guidelines about what to do.

##### Prepare Your Ui for the App Snapshot

After your app enters the background and your delegate method returns, UIKit takes a snapshot of your app’s current user interface. The system displays the resulting image in the app switcher. It also displays the image temporarily when bringing your app back to the foreground.

Your app’s UI must not contain any sensitive user information, such as passwords or credit card numbers. If your interface contains such information, remove it from your views when entering the background. Also, dismiss alerts, temporary interfaces, and system view controllers that obscure your app’s content. The snapshot represents your app’s interface and should be recognizable to users. When your app returns to the foreground, you can restore data and views as appropriate.

> **Note**:  For apps that support state preservation and restoration, the system begins the preservation process shortly after your delegate method returns. Removing sensitive data also prevents that information from being saved in your app’s preservation archive. For more information, see [`Preserving your app’s UI across launches`](preserving-your-app-s-ui-across-launches.md).

##### Respond to Important Events in the Background

Apps don’t normally receive any extra execution time after they enter the background. However, UIKit does grant execution time to apps that support any of the following time-sensitive capabilities:

- Audio communication using AirPlay, or Picture in Picture video.
- Location-sensitive services for users.
- Voice over IP.
- Communication with an external accessory.
- Communication with Bluetooth LE accessories, or conversion of the device into a Bluetooth LE accessory.
- Regular updates from a server.
- Support for Apple Push Notification service (APNs).

Enable the Background Modes capability in Xcode if your app supports background features. Each background task has different requirements; see the appropriate framework for details about how to implement the feature. For information about how to schedule opportunistic background tasks, see [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks).

## Topics

### Background execution
- [Using background tasks to update your app](using-background-tasks-to-update-your-app.md)
  Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [Extending your app’s background execution time](extending-your-app-s-background-execution-time.md)
  Ensure that critical tasks finish when your app moves to the background.
- [About the background execution sequence](about-the-background-execution-sequence.md)
  Learn the order in which your custom code is executed when your app moves to the background.

## See Also

- [Preparing your UI to run in the foreground](preparing-your-ui-to-run-in-the-foreground.md)
  Configure your app to appear onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-background)*