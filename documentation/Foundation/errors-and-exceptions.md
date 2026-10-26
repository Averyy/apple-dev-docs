# Errors and Exceptions

**Framework**: Foundation  
**Role**: API Collection

Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.

## Topics

### User-Relevant Errors
- [protocol Error](../Swift/error.md)
  A type representing an error value that can be thrown.
- [class NSError](./nserror.md)
  Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [protocol LocalizedError](./localizederror.md)
  A specialized error that provides localized messages describing the error and why it occurred.
- [protocol RecoverableError](./recoverableerror.md)
  A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [protocol CustomNSError](./customnserror.md)
  A specialized error that provides a domain, error code, and user-info dictionary.
### Assertions
- [class NSAssertionHandler](./nsassertionhandler.md)
  An object that logs an assertion to the console.
- [NSAssert](./nsassert.md)
  Generates an assertion if a given condition is false.
- [NSAssert1](./nsassert1.md)
  Generates an assertion if a given condition is false.
- [NSAssert2](./nsassert2.md)
  Generates an assertion if a given condition is false.
- [NSAssert3](./nsassert3.md)
  Generates an assertion if a given condition is false.
- [NSAssert4](./nsassert4.md)
  Generates an assertion if a given condition is false.
- [NSAssert5](./nsassert5.md)
  Generates an assertion if a given condition is false.
- [NSCAssert](./nscassert.md)
  Generates an assertion if the given condition is false.
- [NSCAssert1](./nscassert1.md)
  Generates an assertion if a given condition is false.
- [NSCAssert2](./nscassert2.md)
  Generates an assertion if a given condition is false.
- [NSCAssert3](./nscassert3.md)
  Generates an assertion if a given condition is false.
- [NSCAssert4](./nscassert4.md)
  Generates an assertion if a given condition is false.
- [NSCAssert5](./nscassert5.md)
  Generates an assertion if a given condition is false.
- [NSCParameterAssert](./nscparameterassert.md)
  Evaluates the specified parameter.
- [NSParameterAssert](./nsparameterassert.md)
  Validates the specified parameter.
### Exceptions
- [class NSException](./nsexception.md)
  An object that represents a special condition that interrupts the normal flow of program execution.
### Diagnostics and Debugging
- [func NSLogv(String, CVaListPointer)](./nslogv%28_,_%29.md)
  Logs an error message to the Apple System Log facility.
- [func NSLog(String, any CVarArg...)](./nslog%28_,_%29.md)
  Logs an error message to the Apple System Log facility.
- [NSLog](./nslog.md)
  Logs an error message to the Apple System Log facility.
- [NSDeallocateZombies](./nsdeallocatezombies.md)
  A global variable that determines whether or not the memory of zombie objects is deallocated.
- [NSDebugEnabled](./nsdebugenabled.md)
  A global variable that can be used to enable debug behavior in your app, such as extra logging.
- [NSZombieEnabled](./nszombieenabled.md)
  A global variable related to zombie objects that in practice has no effect.
- [NSKeepAllocationStatistics](./nskeepallocationstatistics.md)
  A no-longer-used global variable related to keeping statistics.

## See Also

### App Support
- [Task Management](./task-management.md)
  Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](./resources.md)
  Access assets and other data bundled with your app.
- [Notifications](./notifications.md)
  Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](./app-extension-support.md)
  Manage the interaction between an app extension and its hosting app.
- [Scripting Support](./scripting-support.md)
  Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/errors-and-exceptions)*