# CNGroup

**Framework**: Contacts  
**Kind**: class

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

#### Overview

Contacts may be members of one or more groups, depending upon their accounts.

`CNGroup` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Getting the Group Information
- [var name: String](cngroup/name.md)
  The name of the group.
- [var identifier: String](cngroup/identifier.md)
  The unique identifier for a group on the device.
### Generating Search Predicates for Groups
- [class func predicateForGroups(withIdentifiers: [String]) -> NSPredicate](cngroup/predicateforgroups(withidentifiers:).md)
  Returns a predicate to find groups with the specified identifiers.
- [class func predicateForGroupsInContainer(withIdentifier: String) -> NSPredicate](cngroup/predicateforgroupsincontainer(withidentifier:).md)
  Returns a predicate to find groups in the specified container.
- [class func predicateForSubgroupsInGroup(withIdentifier: String) -> NSPredicate](cngroup/predicateforsubgroupsingroup(withidentifier:).md)
  Returns a predicate to find subgroups in the specified parent group.
### Getting Group-Related Keys
- [let CNGroupIdentifierKey: String](cngroupidentifierkey.md)
  The identifier of the group.
- [let CNGroupNameKey: String](cngroupnamekey.md)
  The name of the group.
### Initializers
- [init?(coder: NSCoder)](cngroup/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CNMutableGroup](cnmutablegroup.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CNMutableGroup](cnmutablegroup.md)
  A mutable object that represents a group of contacts.
- [class CNContainer](cncontainer.md)
  An immutable object that represents a collection of contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup)*