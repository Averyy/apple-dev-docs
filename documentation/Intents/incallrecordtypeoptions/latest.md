# latest

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

The most recent call involving the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var latest: INCallRecordTypeOptions { get }
```

```c
INCallRecordTypeOptionLatest
```

## See Also

### Type Properties
- [static var outgoing: INCallRecordTypeOptions](./outgoing.md)
  A call initiated by the user.
- [static var missed: INCallRecordTypeOptions](./missed.md)
  A call received by the user that went unanswered.
- [static var received: INCallRecordTypeOptions](./received.md)
  A received call that the user answered.
- [static var voicemail: INCallRecordTypeOptions](./voicemail.md)
  A voicemail left from a missed call.
- [static var ringing: INCallRecordTypeOptions](./ringing.md)
  An incoming call that is currently causing the user’s phone to ring.
- [static var inProgress: INCallRecordTypeOptions](./inprogress.md)
  A received call that is currently in progress.
- [static var onHold: INCallRecordTypeOptions](./onhold.md)
  A received call that the user has put on hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtypeoptions/latest)*