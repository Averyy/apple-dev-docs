# INCallGroup

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The details of a group call handled by your app.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
class INCallGroup
```

```objc
@interface INCallGroup : NSObject
```

## Overview

An `INCallGroup` object stores details that the user contributed to your app about a group call. Use call group objects to communicate general information about group calls to SiriKit. An `INCallGroup` identifies the calls group name and unique group ID.

## Topics

### Initializers
- [init?(coder: NSCoder)](./incallgroup/init%28coder%29.md)
- [init(groupName: String?, groupId: String?)](./incallgroup/init%28groupname,groupid%29.md)
  Creates a call record with the group details.
### Instance Properties
- [var groupId: String?](./incallgroup/groupid.md)
  A unique identifier that disguishes call groups.
- [var groupName: String?](./incallgroup/groupname.md)
  The name contributed the user to their group call.

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
- [class INCallRecordFilter](./incallrecordfilter.md)
  Filters a user specifies to redial a call.
- [enum INCallRecordType](./incallrecordtype.md)
  Constants describing the type of the call.
- [struct INCallRecordTypeOptions](./incallrecordtypeoptions.md)
  Constants describing the types of calls to include during a search.
- [enum INCallDestinationType](./incalldestinationtype.md)
  Constants describing the destination of a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallgroup)*