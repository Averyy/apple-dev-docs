# isMicrophoneMuted

**Framework**: GameKit  
**Kind**: property

A Boolean value that determines whether the user’s microphone is muted.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isMicrophoneMuted: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the user’s microphone is turned off; [`false`](https://developer.apple.com/documentation/Swift/false) if the user’s speech is being transmitted to remote participants. The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var remoteParticipantVolume: Float](gkvoicechatservice/remoteparticipantvolume.md)
  A float that scales the volume of all remote participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/ismicrophonemuted)*