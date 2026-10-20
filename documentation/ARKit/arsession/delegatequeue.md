# delegateQueue

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The dispatch queue through which the session calls your delegate methods.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var delegateQueue: dispatch_queue_t? { get set }
```

```objc
@property (nonatomic, strong, nullable) dispatch_queue_t delegateQueue;
```

#### Discussion

If this value is `nil` (the default), the session calls your delegate methods on the main queue.

## See Also

### Responding to events
- [var delegate: (any ARSessionDelegate)?](./delegate.md)
  An object you provide to receive captured video images and tracking information, or to respond to changes in session status.
- [protocol ARSessionDelegate](../arsessiondelegate.md)
  Methods you can implement to receive captured video frame images and tracking state from an AR session.
- [protocol ARSessionObserver](../arsessionobserver.md)
  Methods you can implement to respond to changes in the state of an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/delegatequeue)*