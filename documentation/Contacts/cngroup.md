# CNGroup

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

An immutable object that represents a group of contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNGroup
```

```objc
@interface CNGroup : NSObject
```

#### Overview

Contacts may be members of one or more groups, depending upon their accounts.

`CNGroup` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Getting the Group Information
- [var name: String](./cngroup/name.md)
  The name of the group.
- [var identifier: String](./cngroup/identifier.md)
  The unique identifier for a group on the device.
### Generating Search Predicates for Groups
- [class func predicateForGroups(withIdentifiers: [String]) -> NSPredicate](./cngroup/predicateforgroups%28withidentifiers%29.md)
  Returns a predicate to find groups with the specified identifiers.
- [class func predicateForGroupsInContainer(withIdentifier: String) -> NSPredicate](./cngroup/predicateforgroupsincontainer%28withidentifier%29.md)
  Returns a predicate to find groups in the specified container.
- [class func predicateForSubgroupsInGroup(withIdentifier: String) -> NSPredicate](./cngroup/predicateforsubgroupsingroup%28withidentifier%29.md)
  Returns a predicate to find subgroups in the specified parent group.
### Getting Group-Related Keys
- [let CNGroupIdentifierKey: String](./cngroupidentifierkey.md)
  The identifier of the group.
- [let CNGroupNameKey: String](./cngroupnamekey.md)
  The name of the group.
### Initializers
- [init?(coder: NSCoder)](./cngroup/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CNMutableGroup](./cnmutablegroup.md)
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
- [class CNMutableGroup](./cnmutablegroup.md)
  A mutable object that represents a group of contacts.
- [class CNContainer](./cncontainer.md)
  An immutable object that represents a collection of contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup)*