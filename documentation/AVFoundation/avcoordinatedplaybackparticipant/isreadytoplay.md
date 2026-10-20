# isReadyToPlay

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the participant is ready to start coordinated playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var isReadyToPlay: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isReadyToPlay) BOOL readyToPlay;
```

## See Also

### Accessing participant status
- [var identifier: UUID](./identifier.md)
  A unique identifier for the participant.
- [var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason]](./suspensionreasons.md)
  The reasons a participant isn’t currently participating in coordinated playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant/isreadytoplay)*