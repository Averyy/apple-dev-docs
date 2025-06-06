# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the delegate and a dispatch queue on which the delegate will be called.

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
func setDelegate(_ delegate: (any AVPlayerItemMetadataCollectorPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate`: An object conforming to   protocol.
- `delegateQueue`: A dispatch queue on which all delegate methods will be called.

## See Also

- [var delegate: (any AVPlayerItemMetadataCollectorPushDelegate)?](avplayeritemmetadatacollector/delegate.md)
  Accesses the metadata collector’s delegate object.
- [protocol AVPlayerItemMetadataCollectorPushDelegate](avplayeritemmetadatacollectorpushdelegate.md)
  A protocol you implement to receive metadata callbacks from a player item metadata collector.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadatacollector/delegatequeue.md)
  The dispatch queue on which the delegate’s methods are called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector/setdelegate(_:queue:))*