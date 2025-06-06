# predicateForGroups(withIdentifiers:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find groups with the specified identifiers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForGroups(withIdentifiers identifiers: [String]) -> NSPredicate
```

#### Return Value

A predicate that can be used to fetch groups from [`CNContactStore`](cncontactstore.md).

## Parameters

- `identifiers`: The group identifiers to be matched.

## See Also

- [class func predicateForGroupsInContainer(withIdentifier: String) -> NSPredicate](cngroup/predicateforgroupsincontainer(withidentifier:).md)
  Returns a predicate to find groups in the specified container.
- [class func predicateForSubgroupsInGroup(withIdentifier: String) -> NSPredicate](cngroup/predicateforsubgroupsingroup(withidentifier:).md)
  Returns a predicate to find subgroups in the specified parent group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup/predicateforgroups(withidentifiers:))*