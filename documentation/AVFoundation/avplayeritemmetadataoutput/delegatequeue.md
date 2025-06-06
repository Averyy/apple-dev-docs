# delegateQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue on which messages are sent to the delegate.

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
var delegateQueue: dispatch_queue_t? { get }
```

## See Also

- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [var delegate: (any AVPlayerItemMetadataOutputPushDelegate)?](avplayeritemmetadataoutput/delegate.md)
  The delegate object.
- [protocol AVPlayerItemMetadataOutputPushDelegate](avplayeritemmetadataoutputpushdelegate.md)
  Methods you can implement to provide additional metadata.
- [func setDelegate((any AVPlayerItemMetadataOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemmetadataoutput/setdelegate(_:queue:).md)
  Sets the delegate and a dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/delegatequeue)*