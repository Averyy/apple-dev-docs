# start()

**Framework**: Foundation  
**Kind**: method

Starts the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func start()
```

#### Discussion

This method asynchronously spawns the new thread and invokes the receiver’s [`main()`](thread/main().md) method on the new thread. The [`isExecuting`](thread/isexecuting.md) property returns [`true`](https://developer.apple.com/documentation/Swift/true) once the thread starts executing, which may occur after the [`start()`](thread/start().md) method returns.

If you initialized the receiver with a target and selector, the default [`main()`](thread/main().md) method invokes that selector automatically.

If this thread is the first thread detached in the application, this method posts the [`NSWillBecomeMultiThreaded`](nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with object `nil` to the default notification center.

## See Also

- [convenience init(target: Any, selector: Selector, object: Any?)](thread/init(target:selector:object:).md)
  Returns an `NSThread` object initialized with the given arguments.
- [init()](thread/init.md)
  Returns an initialized `NSThread` object.
- [class func detachNewThreadSelector(Selector, toTarget: Any, with: Any?)](thread/detachnewthreadselector(_:totarget:with:).md)
  Detaches a new thread and uses the specified selector as the thread entry point.
- [func main()](thread/main.md)
  The main entry point routine for the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/start())*