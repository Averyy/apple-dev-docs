# delegate

**Framework**: AVFoundation  
**Kind**: property

The delegate object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
weak var delegate: (any AVPlayerItemMetadataOutputPushDelegate)? { get }
```

## See Also

- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [protocol AVPlayerItemMetadataOutputPushDelegate](avplayeritemmetadataoutputpushdelegate.md)
  Methods you can implement to provide additional metadata.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadataoutput/delegatequeue.md)
  The dispatch queue on which messages are sent to the delegate.
- [func setDelegate((any AVPlayerItemMetadataOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemmetadataoutput/setdelegate(_:queue:).md)
  Sets the delegate and a dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/delegate)*