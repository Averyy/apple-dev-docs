# delegateCallbackQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](../avcapturebroadcastvideooutputdelegate.md) methods will be called.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var delegateCallbackQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t delegateCallbackQueue;
```

#### Discussion

The value of this property is a dispatch queue on which all delegate method calls will be serialized. If you have not called the [`setDelegate(_:queue:)`](./setdelegate%28_,queue%29.md) method, the value of this property will be `nil`.

## See Also

### Related Documentation
- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](./delegate.md)
  The receiver’s delegate.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.
### Managing the Output
- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](./delegate.md)
  The receiver’s delegate.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/delegatecallbackqueue)*