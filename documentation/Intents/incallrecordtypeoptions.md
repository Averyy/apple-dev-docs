# INCallRecordTypeOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants describing the types of calls to include during a search.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
struct INCallRecordTypeOptions
```

```c
enum INCallRecordTypeOptions : NSUInteger;
```

## Topics

### Type Properties
- [static var outgoing: INCallRecordTypeOptions](./incallrecordtypeoptions/outgoing.md)
  A call initiated by the user.
- [static var missed: INCallRecordTypeOptions](./incallrecordtypeoptions/missed.md)
  A call received by the user that went unanswered.
- [static var received: INCallRecordTypeOptions](./incallrecordtypeoptions/received.md)
  A received call that the user answered.
- [static var latest: INCallRecordTypeOptions](./incallrecordtypeoptions/latest.md)
  The most recent call involving the user.
- [static var voicemail: INCallRecordTypeOptions](./incallrecordtypeoptions/voicemail.md)
  A voicemail left from a missed call.
- [static var ringing: INCallRecordTypeOptions](./incallrecordtypeoptions/ringing.md)
  An incoming call that is currently causing the user’s phone to ring.
- [static var inProgress: INCallRecordTypeOptions](./incallrecordtypeoptions/inprogress.md)
  A received call that is currently in progress.
- [static var onHold: INCallRecordTypeOptions](./incallrecordtypeoptions/onhold.md)
  A received call that the user has put on hold.
### Initializers
- [init(rawValue: UInt)](./incallrecordtypeoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Describing a Call
- [class INCallRecord](./incallrecord.md)
  The details about a call handled by your app.
- [class INCallGroup](./incallgroup.md)
  The details of a group call handled by your app.
- [class INCallRecordFilter](./incallrecordfilter.md)
  Filters a user specifies to redial a call.
- [enum INCallRecordType](./incallrecordtype.md)
  Constants describing the type of the call.
- [enum INCallDestinationType](./incalldestinationtype.md)
  Constants describing the destination of a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordtypeoptions)*