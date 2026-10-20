# predicateForSubgroupsInGroup(withIdentifier:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

Returns a predicate to find subgroups in the specified parent group.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class func predicateForSubgroupsInGroup(withIdentifier parentGroupIdentifier: String) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForSubgroupsInGroupWithIdentifier:(NSString *) parentGroupIdentifier;
```

#### Return Value

A predicate that you can use to fetch subgroup information from [`CNContactStore`](../cncontactstore.md).

## Parameters

- `parentGroupIdentifier`: The parent group to be matched.

## See Also

### Generating Search Predicates for Groups
- [class func predicateForGroups(withIdentifiers: [String]) -> NSPredicate](./predicateforgroups%28withidentifiers%29.md)
  Returns a predicate to find groups with the specified identifiers.
- [class func predicateForGroupsInContainer(withIdentifier: String) -> NSPredicate](./predicateforgroupsincontainer%28withidentifier%29.md)
  Returns a predicate to find groups in the specified container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup/predicateforsubgroupsingroup(withidentifier:))*