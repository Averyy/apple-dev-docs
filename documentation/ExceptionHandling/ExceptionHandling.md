# Exception Handling

**Framework**: Exception Handling  
**Kind**: module

Monitor and debug exceptional conditions in code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

#### Overview

This collection of documents provides the API reference for the Exception Handling framework. This framework provides facilities for monitoring and debugging exceptional conditions in Objective-C code.

Currently only one class reference is part of this collection: the reference for the [`NSExceptionHandler`](nsexceptionhandler.md) class, which is defined in `NSExceptionHandler.h`.

## Topics

### Classes
- [class NSExceptionHandler](nsexceptionhandler.md)
  The `NSExceptionHandler` class provides facilities for monitoring and debugging exceptional conditions in Objective-C programs. It works by installing a special uncaught exception handler via the  [`NSSetUncaughtExceptionHandler(_:)`](https://developer.apple.com/documentation/Foundation/NSSetUncaughtExceptionHandler(_:)) function. Consequently, to use the services of `NSExceptionHandler`, you must not install your own custom uncaught exception handler.
### Protocols
- [NSExceptionHandlerDelegate](nsexceptionhandlerdelegate.md)
  The `NSExceptionHandlerDelegate` informal protocol describes methods that [`NSExceptionHandler`](nsexceptionhandler.md) objects call on their delegates when exceptions occur. An [`NSExceptionHandler`](nsexceptionhandler.md) object does not need to have a delegate. When one does, these delegate methods are asked to approve exception handling and logging for each monitored [`NSExceptionHandler`](nsexceptionhandler.md) object.
### Reference
- [ExceptionHandling Enumerations](exceptionhandling-enumerations.md)
- [ExceptionHandling Constants](exceptionhandling-constants.md)
- [ExceptionHandling Functions](exceptionhandling-functions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExceptionHandling)*