# INCallRecordFilter

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Filters a user specifies to redial a call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INCallRecordFilter
```

```objc
@interface INCallRecordFilter : NSObject
```

## Overview

Use this method to create filters contributed by the user to redial a call. The `INCallRecordFilter` object identifies the person, type of call, and ability to make the call to initiate the user’s request.

## Topics

### Initializers
- [init?(coder: NSCoder)](./incallrecordfilter/init%28coder%29.md)
- [init(participants: [INPerson]?, callTypes: INCallRecordTypeOptions, callCapability: INCallCapability)](./incallrecordfilter/init%28participants,calltypes,callcapability%29.md)
  Creates a filtered call record with the details about a call.
### Instance Properties
- [var callCapability: INCallCapability](./incallrecordfilter/callcapability.md)
  An indicator of whether the call supports audio or video.
- [var callTypes: INCallRecordTypeOptions](./incallrecordfilter/calltypes.md)
  The various call options that the user can requests.
- [var participants: [INPerson]?](./incallrecordfilter/participants.md)
  The recipient of the user’s call request.

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
- [class INCallRecord](./incallrecord.md)
  The details about a call handled by your app.
- [class INCallGroup](./incallgroup.md)
  The details of a group call handled by your app.
- [enum INCallRecordType](./incallrecordtype.md)
  Constants describing the type of the call.
- [struct INCallRecordTypeOptions](./incallrecordtypeoptions.md)
  Constants describing the types of calls to include during a search.
- [enum INCallDestinationType](./incalldestinationtype.md)
  Constants describing the destination of a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordfilter)*