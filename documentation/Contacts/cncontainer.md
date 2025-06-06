# CNContainer

**Framework**: Contacts  
**Kind**: class

An immutable object that represents a collection of contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContainer
```

#### Overview

A contact can be in only one container. CardDAV accounts usually have only one container whereas Exchange accounts may have multiple containers, where each container represents an Exchange folder.

`CNContainer` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Getting the Container Information
- [var name: String](cncontainer/name.md)
  The name of the container.
- [var identifier: String](cncontainer/identifier.md)
  The unique identifier for a contacts container on the device.
- [var type: CNContainerType](cncontainer/type.md)
  The type of the container.
- [enum CNContainerType](cncontainertype.md)
  The container may be local on the device or associated with a server account that has contacts.
### Generating Search Predicates for Containers
- [class func predicateForContainerOfContact(withIdentifier: String) -> NSPredicate](cncontainer/predicateforcontainerofcontact(withidentifier:).md)
  Returns a predicate to find the container of the specified contact.
- [class func predicateForContainers(withIdentifiers: [String]) -> NSPredicate](cncontainer/predicateforcontainers(withidentifiers:).md)
  Returns a predicate to find the containers with the specified identifiers.
- [class func predicateForContainerOfGroup(withIdentifier: String) -> NSPredicate](cncontainer/predicateforcontainerofgroup(withidentifier:).md)
  Returns a predicate to find the container of the specified group.
### Getting Container-Related Keys
- [let CNContainerIdentifierKey: String](cncontaineridentifierkey.md)
  The identifier key of the container.
- [let CNContainerNameKey: String](cncontainernamekey.md)
  The name of the container.
- [let CNContainerTypeKey: String](cncontainertypekey.md)
  The type of the container.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNGroup](cngroup.md)
  An immutable object that represents a group of contacts.
- [class CNMutableGroup](cnmutablegroup.md)
  A mutable object that represents a group of contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer)*