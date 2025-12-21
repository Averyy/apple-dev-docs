# Errors and Exceptions

**Framework**: Foundation

Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.

## Topics

### User-Relevant Errors
- [protocol Error](../Swift/Error.md)
  A type representing an error value that can be thrown.
- [class NSError](nserror.md)
  Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [protocol LocalizedError](localizederror.md)
  A specialized error that provides localized messages describing the error and why it occurred.
- [protocol RecoverableError](recoverableerror.md)
  A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [protocol CustomNSError](customnserror.md)
  A specialized error that provides a domain, error code, and user-info dictionary.
### Assertions
- [class NSAssertionHandler](nsassertionhandler.md)
  An object that logs an assertion to the console.
### Exceptions
- [class NSException](nsexception.md)
  An object that represents a special condition that interrupts the normal flow of program execution.
### Diagnostics and Debugging
- [func NSLogv(String, CVaListPointer)](nslogv(_:_:).md)
  Logs an error message to the Apple System Log facility.
- [func NSLog(String, any CVarArg...)](nslog(_:_:).md)
  Logs an error message to the Apple System Log facility.

## See Also

- [Task Management](task-management.md)
  Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](resources.md)
  Access assets and other data bundled with your app.
- [Notifications](notifications.md)
  Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](app-extension-support.md)
  Manage the interaction between an app extension and its hosting app.
- [Scripting Support](scripting-support.md)
  Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/errors-and-exceptions)*