# isMicrophoneMuted

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user’s microphone is muted.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
var isMicrophoneMuted: Bool { get set }
```

```objc
@property (nonatomic, getter=isMicrophoneMuted) BOOL microphoneMuted;
```

## Discussion

[`true`](../../Swift/true.md) if the user’s microphone is turned off; [`false`](../../Swift/false.md) if the user’s speech is being transmitted to remote participants. The default is [`false`](../../Swift/false.md).

## See Also

### Adjusting Audio Properties
- [var remoteParticipantVolume: Float](./remoteparticipantvolume.md)
  A float that scales the volume of all remote participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/ismicrophonemuted)*