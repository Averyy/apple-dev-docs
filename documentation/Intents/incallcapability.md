# INCallCapability

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the capabilities of the call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INCallCapability
```

```c
enum INCallCapability : NSInteger;
```

## Topics

### Constants
- [INCallCapability.unknown](./incallcapability/unknown.md)
  An unknown type of call.
- [INCallCapability.audioCall](./incallcapability/audiocall.md)
  An audio call.
- [INCallCapability.videoCall](./incallcapability/videocall.md)
  A video call.
### Initializers
- [init?(rawValue: Int)](./incallcapability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Call Details
- [var callRecordType: INCallRecordType](./incallrecord/callrecordtype.md)
  The type of call that resulted from the attempt.
- [var callCapability: INCallCapability](./incallrecord/callcapability.md)
  The audio and video capabilities of the call.
- [var dateCreated: Date?](./incallrecord/datecreated.md)
  The date and time at which the call was initiated.
- [var callDuration: Double?](./incallrecord/callduration-47iud.md)
  The duration (measured in seconds) of the call.
- [var unseen: Bool?](./incallrecord/unseen-2m7sz.md)
  A Boolean value indicating whether the user has seen the call.
- [var numberOfCalls: Int?](./incallrecord/numberofcalls-r8kl.md)
  The number of calls in the call record.
- [var participants: [INPerson]?](./incallrecord/participants.md)
  The recipient of the user’s call request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallcapability)*