# visitAddMember(_:)

**Framework**: Contacts  
**Kind**: method

Tells the delegate that the user added a contact to a group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func visitAddMember(_ event: CNChangeHistoryAddMemberToGroupEvent)
```

#### Discussion

Inspect the group and contact in the event that the system provides and update your app’s cached data accordingly.

## Parameters

- `event`: The event object that represents a user adding a contact to a group.

## See Also

- [func visitRemoveMember(CNChangeHistoryRemoveMemberFromGroupEvent)](cnchangehistoryeventvisitor/visitremovemember(_:).md)
  Tells the delegate that the user removed a contact from a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visitaddmember(_:))*