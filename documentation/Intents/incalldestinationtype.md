# INCallDestinationType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants describing the destination of a call.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INCallDestinationType
```

```c
enum INCallDestinationType : NSInteger;
```

## Topics

### Constants
- [INCallDestinationType.unknown](./incalldestinationtype/unknown.md)
  An unknown call destination.
- [INCallDestinationType.normal](./incalldestinationtype/normal.md)
  A call routed to its expected destination.
- [INCallDestinationType.emergency](./incalldestinationtype/emergency.md)
  A call routed to an emergency number.
- [INCallDestinationType.voicemail](./incalldestinationtype/voicemail.md)
  A call routed to the user’s voicemail.
- [INCallDestinationType.redial](./incalldestinationtype/redial.md)
  A call that was the result of redialing a previous call.
- [INCallDestinationType.callBack](./incalldestinationtype/callback.md)
  A call that was the result of a call back.
- [static var normalDestination: INCallDestinationType](./incalldestinationtype/normaldestination.md)
  A call routed to its expected destination.
- [static var emergencyDestination: INCallDestinationType](./incalldestinationtype/emergencydestination.md)
  A call routed to an emergency number.
- [static var voicemailDestination: INCallDestinationType](./incalldestinationtype/voicemaildestination.md)
  A call routed to the user’s voicemail.
- [static var redialDestination: INCallDestinationType](./incalldestinationtype/redialdestination.md)
  A call that was the result of redialing a previous call.
### Initializers
- [init?(rawValue: Int)](./incalldestinationtype/init%28rawvalue%29.md)

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
- [enum INCallRecordType](./incallrecordtype.md)
  Constants describing the type of the call.
- [struct INCallRecordTypeOptions](./incallrecordtypeoptions.md)
  Constants describing the types of calls to include during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incalldestinationtype)*