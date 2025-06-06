# Notifications

**Framework**: Foundation

Design patterns for broadcasting information and for subscribing to broadcasts.

## Topics

### Key-Value Observing
- [NSKeyValueObserving](../ObjectiveC/nskeyvalueobserving.md)
  An informal protocol that objects adopt to be notified of changes to the specified properties of other objects.
### Notifications
- [struct Notification](notification.md)
  A container for information broadcast through a notification center to all registered observers.
- [class NotificationCenter](notificationcenter.md)
  A notification dispatch mechanism that enables the broadcast of information to registered observers.
- [class NotificationQueue](notificationqueue.md)
  A notification center buffer.
### Cross-Process Notifications
- [class DistributedNotificationCenter](distributednotificationcenter.md)
  A notification dispatch mechanism that enables the broadcast of notifications across task boundaries.

## See Also

- [Task Management](task-management.md)
  Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](resources.md)
  Access assets and other data bundled with your app.
- [App Extension Support](app-extension-support.md)
  Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](errors-and-exceptions.md)
  Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](scripting-support.md)
  Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notifications)*