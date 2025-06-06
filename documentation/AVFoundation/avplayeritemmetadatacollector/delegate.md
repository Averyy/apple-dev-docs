# delegate

**Framework**: AVFoundation  
**Kind**: property

Accesses the metadata collector’s delegate object.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.3+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.3+

## Declaration

```swift
weak var delegate: (any AVPlayerItemMetadataCollectorPushDelegate)? { get }
```

#### Discussion

The delegate is held using a zeroing-weak reference, so this property will have a value of `nil` after a delegate that was previously set has been deallocated.

This property is not key-value observable.

## See Also

- [func setDelegate((any AVPlayerItemMetadataCollectorPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemmetadatacollector/setdelegate(_:queue:).md)
  Sets the delegate and a dispatch queue on which the delegate will be called.
- [protocol AVPlayerItemMetadataCollectorPushDelegate](avplayeritemmetadatacollectorpushdelegate.md)
  A protocol you implement to receive metadata callbacks from a player item metadata collector.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadatacollector/delegatequeue.md)
  The dispatch queue on which the delegate’s methods are called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/delegate)*