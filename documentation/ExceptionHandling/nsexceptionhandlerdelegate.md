# NSExceptionHandlerDelegate

**Framework**: Exception Handling

The `NSExceptionHandlerDelegate` informal protocol describes methods that [`NSExceptionHandler`](nsexceptionhandler.md) objects call on their delegates when exceptions occur. An [`NSExceptionHandler`](nsexceptionhandler.md) object does not need to have a delegate. When one does, these delegate methods are asked to approve exception handling and logging for each monitored [`NSExceptionHandler`](nsexceptionhandler.md) object.

## Topics

### Logging and handling exceptions
- [func exceptionHandler(_ sender: NSExceptionHandler!, shouldHandle exception: NSException!, mask aMask: Int) -> Bool](../ObjectiveC/NSObject-swift.class/exceptionHandler(_:shouldHandle:mask:).md)
  Implemented by the delegate to evaluate whether the delegating exception handler should handle a given exception.
- [func exceptionHandler(_ sender: NSExceptionHandler!, shouldLogException exception: NSException!, mask aMask: Int) -> Bool](../ObjectiveC/NSObject-swift.class/exceptionHandler(_:shouldLogException:mask:).md)
  Implemented by the delegate to evaluate whether the delegating exception hangler should log a given exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandlerdelegate)*