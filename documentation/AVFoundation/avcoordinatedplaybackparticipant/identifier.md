# identifier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the participant.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: UUID { get }
```

```objc
@property (nonatomic, readonly) NSUUID * identifier;
```

## See Also

### Accessing participant status
- [var isReadyToPlay: Bool](./isreadytoplay.md)
  A Boolean value that indicates whether the participant is ready to start coordinated playback.
- [var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason]](./suspensionreasons.md)
  The reasons a participant isn’t currently participating in coordinated playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant/identifier)*