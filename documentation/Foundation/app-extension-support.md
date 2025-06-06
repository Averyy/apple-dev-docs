# App Extension Support

**Framework**: Foundation

Manage the interaction between an app extension and its hosting app.

## Topics

### Extension Support
- [protocol NSExtensionRequestHandling](nsextensionrequesthandling.md)
  The interface an app extension uses to respond to a request from a host app.
- [class NSExtensionContext](nsextensioncontext.md)
  The host app context from which an app extension is invoked.
### Share Extensions
- [Supporting suggestions in your app’s share extension](supporting-suggestions-in-your-app-s-share-extension.md)
  Make your messaging app available for share sheet suggestions and use SiriKit intents to populate your app’s share extension.
### Attachments
- [class NSItemProvider](nsitemprovider.md)
  An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.
- [class NSExtensionItem](nsextensionitem.md)
  An immutable collection of values representing different aspects of an item for an extension to act upon.
- [Add Functionality to Finder with Action Extensions](../AppKit/add-functionality-to-finder-with-action-extensions.md)
  Implement Action Extensions to provide quick access to commonly used features of your app.
### Host App Interaction
- [class NSUserActivity](nsuseractivity.md)
  A representation of the state of your app at a moment in time.
- [protocol NSUserActivityDelegate](nsuseractivitydelegate.md)
  The interface through which a user activity instance notifies its delegate of updates.

## See Also

- [Task Management](task-management.md)
  Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](resources.md)
  Access assets and other data bundled with your app.
- [Notifications](notifications.md)
  Design patterns for broadcasting information and for subscribing to broadcasts.
- [Errors and Exceptions](errors-and-exceptions.md)
  Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](scripting-support.md)
  Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/app-extension-support)*