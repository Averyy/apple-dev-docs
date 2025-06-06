# Task Management

**Framework**: Foundation

Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.

## Topics

### Undo
- [class UndoManager](undomanager.md)
  A general-purpose recorder of operations that enables undo and redo.
### Progress
- [protocol ProgressReporting](progressreporting.md)
  An interface for objects that report progress using a single progress instance.
- [class Progress](progress.md)
  An object that conveys ongoing progress to the user for a specified task.
### Operations
- [class Operation](operation.md)
  An abstract class that represents the code and data associated with a single task.
- [class OperationQueue](operationqueue.md)
  A queue that regulates the execution of operations.
- [class BlockOperation](blockoperation.md)
  An operation that manages the concurrent execution of one or more blocks.
### Scheduling
- [class Timer](timer.md)
  A timer that fires after a certain time interval has elapsed, sending a specified message to a target object.
### Activity Sharing
- [Increasing App Usage with Suggestions Based on User Activities](task_management/increasing_app_usage_with_suggestions_based_on_user_activities.md)
  Provide a continuous user experience by capturing information from your app and displaying this information as proactive suggestions across the system.
- [Continuing User Activities with Handoff](continuing-user-activities-with-handoff.md)
  Define and manage which of your app’s activities can be continued between devices.
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)
  Create, send, and receive user activities directly.
- [class NSUserActivity](nsuseractivity.md)
  A representation of the state of your app at a moment in time.
- [protocol NSUserActivityDelegate](nsuseractivitydelegate.md)
  The interface through which a user activity instance notifies its delegate of updates.
### System Interaction
- [class ProcessInfo](processinfo.md)
  A collection of information about the current process.
- [class NSBackgroundActivityScheduler](nsbackgroundactivityscheduler.md)
  A task scheduler suitable for low priority operations that can run in the background.
### User Notifications
- [class NSUserNotification](nsusernotification.md)
  A notification that can be scheduled for display in the notification center.
- [class NSUserNotificationAction](nsusernotificationaction.md)
  An action that the user can take in response to receiving a notification.
- [class NSUserNotificationCenter](nsusernotificationcenter.md)
  An object that delivers notifications from apps to the user.
- [protocol NSUserNotificationCenterDelegate](nsusernotificationcenterdelegate.md)
  An interface that enables customizing the behavior of the default notification center.
### Combine Integration
- [typealias Published](published.md)
  A type alias for the Combine framework’s type that publishes a property marked with an attribute.
- [typealias ObservableObject](observableobject.md)
  A type alias for the Combine framework’s type for an object with a publisher that emits before the object has changed.

## See Also

- [Resources](resources.md)
  Access assets and other data bundled with your app.
- [Notifications](notifications.md)
  Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](app-extension-support.md)
  Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](errors-and-exceptions.md)
  Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](scripting-support.md)
  Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/task-management)*