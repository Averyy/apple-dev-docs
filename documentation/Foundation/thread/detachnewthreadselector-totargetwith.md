# detachNewThreadSelector(_:toTarget:with:)

**Framework**: Foundation  
**Kind**: method

Detaches a new thread and uses the specified selector as the thread entry point.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func detachNewThreadSelector(_ selector: Selector, toTarget target: Any, with argument: Any?)
```

#### Discussion

The objects `aTarget` and `anArgument` are retained during the execution of the detached thread, then released. The detached thread is exited (using the [`exit()`](thread/exit().md) class method) as soon as `aTarget` has completed executing the `aSelector` method.

If this thread is the first thread detached in the application, this method posts the [`NSWillBecomeMultiThreaded`](nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with object `nil` to the default notification center.

## Parameters

- `selector`: The selector for the message to send to the target. This selector must take only one argument and must not have a return value.
- `target`: The object that will receive the message   on the new thread.
- `argument`: The single argument passed to the target. May be  .

## See Also

- [class func isMultiThreaded() -> Bool](thread/ismultithreaded.md)
  Returns whether the application is multithreaded.
- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [func start()](thread/start.md)
  Starts the receiver.
- [func main()](thread/main.md)
  The main entry point routine for the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/detachnewthreadselector(_:totarget:with:))*