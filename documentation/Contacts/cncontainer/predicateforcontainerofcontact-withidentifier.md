# predicateForContainerOfContact(withIdentifier:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find the container of the specified contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForContainerOfContact(withIdentifier contactIdentifier: String) -> NSPredicate
```

#### Return Value

A predicate that can be used to fetch a container from [`CNContactStore`](cncontactstore.md).

#### Discussion

If the identifier is for a unified contact then this method returns an empty array. To fetch the containers of a unified contact, first fetch the linked contacts and then fetch the container of each linked contact.

## Parameters

- `contactIdentifier`: The contact identifier to be matched.

## See Also

- [class func predicateForContainers(withIdentifiers: [String]) -> NSPredicate](cncontainer/predicateforcontainers(withidentifiers:).md)
  Returns a predicate to find the containers with the specified identifiers.
- [class func predicateForContainerOfGroup(withIdentifier: String) -> NSPredicate](cncontainer/predicateforcontainerofgroup(withidentifier:).md)
  Returns a predicate to find the container of the specified group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/predicateforcontainerofcontact(withidentifier:))*