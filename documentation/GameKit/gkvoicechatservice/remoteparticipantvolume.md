# remoteParticipantVolume

**Framework**: GameKit  
**Kind**: property

A float that scales the volume of all remote participants.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var remoteParticipantVolume: Float { get set }
```

#### Discussion

The value should be between `0.0` (muted) and `1.0` (full volume). The default is `1.0`.

## See Also

- [var isMicrophoneMuted: Bool](gkvoicechatservice/ismicrophonemuted.md)
  A Boolean value that determines whether the user’s microphone is muted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/remoteparticipantvolume)*