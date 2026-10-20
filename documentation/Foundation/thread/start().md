# start()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) start;
```

#### Discussion

This method asynchronously spawns the new thread and invokes the receiver’s [`main()`](./main%28%29.md) method on the new thread. The [`isExecuting`](./isexecuting.md) property returns [`true`](../../Swift/true.md) once the thread starts executing, which may occur after the [`start()`](./start%28%29.md) method returns.

If you initialized the receiver with a target and selector, the default [`main()`](./main%28%29.md) method invokes that selector automatically.

If this thread is the first thread detached in the application, this method posts the [`NSWillBecomeMultiThreaded`](../nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with object `nil` to the default notification center.

## See Also

### Related Documentation
- [convenience init(target: Any, selector: Selector, object: Any?)](./init%28target,selector,object%29.md)
  Returns an `NSThread` object initialized with the given arguments.
- [init()](./init%28%29.md)
  Returns an initialized `NSThread` object.
### Starting a Thread
- [class func detachNewThreadSelector(Selector, toTarget: Any, with: Any?)](./detachnewthreadselector%28_,totarget,with%29.md)
  Detaches a new thread and uses the specified selector as the thread entry point.
- [func main()](./main%28%29.md)
  The main entry point routine for the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/start())*