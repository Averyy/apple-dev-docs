# predicateForGroupsInContainer(withIdentifier:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find groups in the specified container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForGroupsInContainer(withIdentifier containerIdentifier: String) -> NSPredicate
```

#### Return Value

A predicate that you can use to fetch groups from [`CNContactStore`](cncontactstore.md).

## Parameters

- `containerIdentifier`: The container identifier to be matched.

## See Also

- [class func predicateForGroups(withIdentifiers: [String]) -> NSPredicate](cngroup/predicateforgroups(withidentifiers:).md)
  Returns a predicate to find groups with the specified identifiers.
- [class func predicateForSubgroupsInGroup(withIdentifier: String) -> NSPredicate](cngroup/predicateforsubgroupsingroup(withidentifier:).md)
  Returns a predicate to find subgroups in the specified parent group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup/predicateforgroupsincontainer(withidentifier:))*