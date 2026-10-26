# INCallRecord

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The details about a call handled by your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INCallRecord
```

```objc
@interface INCallRecord : NSObject
```

#### Overview

An `INCallRecord` object stores details about calls made by the user through your app. You use call record objects to communicate basic information about calls to SiriKit. A call record identifies the type of call, the duration of the call, the date and time of the call, and the person on the other end of the call. You create call record objects when reporting search results back to SiriKit and when identifying voicemails to play.

## Topics

### Initializing a Call Record
- [convenience init(identifier: String, dateCreated: Date?, caller: INPerson?, callRecordType: INCallRecordType, callCapability: INCallCapability, callDuration: Double?, unseen: Bool?, numberOfCalls: Int?)](./incallrecord/init%28identifier,datecreated,caller,callrecordtype,callcapability,callduration,unseen,numberofcalls%29.md)
  Creates a call record with the details about the call.
### Identifying the Call
- [var identifier: String](./incallrecord/identifier.md)
  A unique string that you can use to locate the call in your app.
### Identifying the Caller
- [var caller: INPerson?](./incallrecord/caller.md)
  The person who participated in the call with the current user.
### Getting the Call Details
- [var callRecordType: INCallRecordType](./incallrecord/callrecordtype.md)
  The type of call that resulted from the attempt.
- [var callCapability: INCallCapability](./incallrecord/callcapability.md)
  The audio and video capabilities of the call.
- [enum INCallCapability](./incallcapability.md)
  Constants indicating the capabilities of the call.
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
### Initializers
- [init?(coder: NSCoder)](./incallrecord/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Describing a Call
- [class INCallGroup](./incallgroup.md)
  The details of a group call handled by your app.
- [class INCallRecordFilter](./incallrecordfilter.md)
  Filters a user specifies to redial a call.
- [enum INCallRecordType](./incallrecordtype.md)
  Constants describing the type of the call.
- [struct INCallRecordTypeOptions](./incallrecordtypeoptions.md)
  Constants describing the types of calls to include during a search.
- [enum INCallDestinationType](./incalldestinationtype.md)
  Constants describing the destination of a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord)*