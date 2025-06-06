# predicateForContainerOfGroup(withIdentifier:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find the container of the specified group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForContainerOfGroup(withIdentifier groupIdentifier: String) -> NSPredicate
```

#### Return Value

A predicate that can be used to fetch a container from [`CNContactStore`](cncontactstore.md).

## Parameters

- `groupIdentifier`: The group identifier to be matched.

## See Also

- [class func predicateForContainerOfContact(withIdentifier: String) -> NSPredicate](cncontainer/predicateforcontainerofcontact(withidentifier:).md)
  Returns a predicate to find the container of the specified contact.
- [class func predicateForContainers(withIdentifiers: [String]) -> NSPredicate](cncontainer/predicateforcontainers(withidentifiers:).md)
  Returns a predicate to find the containers with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/predicateforcontainerofgroup(withidentifier:))*