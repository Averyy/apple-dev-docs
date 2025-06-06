# predicateForSubgroupsInGroup(withIdentifier:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find subgroups in the specified parent group.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class func predicateForSubgroupsInGroup(withIdentifier parentGroupIdentifier: String) -> NSPredicate
```

#### Return Value

A predicate that you can use to fetch subgroup information from [`CNContactStore`](cncontactstore.md).

## Parameters

- `parentGroupIdentifier`: The parent group to be matched.

## See Also

- [class func predicateForGroups(withIdentifiers: [String]) -> NSPredicate](cngroup/predicateforgroups(withidentifiers:).md)
  Returns a predicate to find groups with the specified identifiers.
- [class func predicateForGroupsInContainer(withIdentifier: String) -> NSPredicate](cngroup/predicateforgroupsincontainer(withidentifier:).md)
  Returns a predicate to find groups in the specified container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup/predicateforsubgroupsingroup(withidentifier:))*