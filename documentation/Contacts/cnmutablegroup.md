# CNMutableGroup

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

A mutable object that represents a group of contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNMutableGroup
```

```objc
@interface CNMutableGroup : CNGroup
```

## Overview

Contacts may be members of one or more groups, depending upon the accounts they come from. The `CNMutableGroup` class is not a thread-safe class.

## Topics

### Modifying the Group Name
- [var name: String](./cnmutablegroup/name.md)
  The name of the group.

## Relationships

### Inherits From
- [CNGroup](./cngroup.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Groups and Containers
- [class CNGroup](./cngroup.md)
  An immutable object that represents a group of contacts.
- [class CNContainer](./cncontainer.md)
  An immutable object that represents a collection of contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablegroup)*