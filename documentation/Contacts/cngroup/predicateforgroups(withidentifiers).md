# predicateForGroups(withIdentifiers:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSPredicate *) predicateForGroupsWithIdentifiers:(NSArray<NSString *> *) identifiers;
```

#### Return Value

A predicate that can be used to fetch groups from [`CNContactStore`](../cncontactstore.md).

## Parameters

- `identifiers`: The group identifiers to be matched.

## See Also

### Generating Search Predicates for Groups
- [class func predicateForGroupsInContainer(withIdentifier: String) -> NSPredicate](./predicateforgroupsincontainer%28withidentifier%29.md)
  Returns a predicate to find groups in the specified container.
- [class func predicateForSubgroupsInGroup(withIdentifier: String) -> NSPredicate](./predicateforsubgroupsingroup%28withidentifier%29.md)
  Returns a predicate to find subgroups in the specified parent group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cngroup/predicateforgroups(withidentifiers:))*