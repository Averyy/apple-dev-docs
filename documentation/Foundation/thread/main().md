# main()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

The main entry point routine for the thread.

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
func main()
```

```objc
- (void) main;
```

#### Discussion

The default implementation of this method takes the target and selector used to initialize the receiver and invokes the selector on the specified target. If you subclass `NSThread`, you can override this method and use it to implement the main body of your thread instead. If you do so, you do not need to invoke `super`.

You should never invoke this method directly. You should always start your thread by invoking the [`start()`](./start%28%29.md) method.

## See Also

### Starting a Thread
- [class func detachNewThreadSelector(Selector, toTarget: Any, with: Any?)](./detachnewthreadselector%28_,totarget,with%29.md)
  Detaches a new thread and uses the specified selector as the thread entry point.
- [func start()](./start%28%29.md)
  Starts the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/main())*