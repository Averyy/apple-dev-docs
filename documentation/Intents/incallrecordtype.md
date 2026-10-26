# INCallRecordType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants describing the type of the call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INCallRecordType
```

```c
enum INCallRecordType : NSInteger;
```

## Topics

### Constants
- [INCallRecordType.unknown](./incallrecordtype/unknown.md)
  An unknown type of call.
- [INCallRecordType.outgoing](./incallrecordtype/outgoing.md)
  A call initiated by the current user.
- [INCallRecordType.missed](./incallrecordtype/missed.md)
  A received call that the user did not answer.
- [INCallRecordType.received](./incallrecordtype/received.md)
  A received call that the user answered.
- [INCallRecordType.latest](./incallrecordtype/latest.md)
  The most recent call involving the user.
- [INCallRecordType.voicemail](./incallrecordtype/voicemail.md)
  A voicemail left from a missed call.
- [INCallRecordType.inProgress](./incallrecordtype/inprogress.md)
  A received call that is currently in progress.
- [INCallRecordType.onHold](./incallrecordtype/onhold.md)
  A received call that the user has put on hold.
- [INCallRecordType.ringing](./incallrecordtype/ringing.md)
  An incoming call that is currently causing the user’s phone to ring.
### Initializers
- [init?(rawValue: Int)](./incallrecordtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Describing a Call
- [class INCallRecord](./incallrecord.md)
  The details about a call handled by your app.
- [class INCallGroup](./incallgroup.md)
  The details of a group call handled by your app.
- [class INCallRecordFilter](./incallrecordfilter.md)
  Filters a user specifies to redial a call.
- [struct INCallRecordTypeOptions](./incallrecordtypeoptions.md)
  Constants describing the types of calls to include during a search.
- [enum INCallDestinationType](./incalldestinationtype.md)
  Constants describing the destination of a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtype)*