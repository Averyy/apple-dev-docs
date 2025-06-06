# visitRemoveSubgroup(_:)

**Framework**: Contacts  
**Kind**: method

Tells the delegate that the user removed a subgroup from a group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func visitRemoveSubgroup(_ event: CNChangeHistoryRemoveSubgroupFromGroupEvent)
```

#### Discussion

Inspect the group and subgroup in the event that the system provides and update your app’s cached data accordingly.

## Parameters

- `event`: The event object that represents a user removing a subgroup from a group.

## See Also

- [func visitAddSubgroup(CNChangeHistoryAddSubgroupToGroupEvent)](cnchangehistoryeventvisitor/visitaddsubgroup(_:).md)
  Tells the delegate that the user added a subgroup to a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visitremovesubgroup(_:))*