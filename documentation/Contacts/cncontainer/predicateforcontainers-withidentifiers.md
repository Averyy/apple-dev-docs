# predicateForContainers(withIdentifiers:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find the containers with the specified identifiers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForContainers(withIdentifiers identifiers: [String]) -> NSPredicate
```

#### Return Value

A predicate that can be used to fetch containers from [`CNContactStore`](cncontactstore.md).

## Parameters

- `identifiers`: The container identifiers to be matched.

## See Also

- [class func predicateForContainerOfContact(withIdentifier: String) -> NSPredicate](cncontainer/predicateforcontainerofcontact(withidentifier:).md)
  Returns a predicate to find the container of the specified contact.
- [class func predicateForContainerOfGroup(withIdentifier: String) -> NSPredicate](cncontainer/predicateforcontainerofgroup(withidentifier:).md)
  Returns a predicate to find the container of the specified group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/predicateforcontainers(withidentifiers:))*