# visitRemoveMember(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user removed a contact from a group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func visitRemoveMember(_ event: CNChangeHistoryRemoveMemberFromGroupEvent)
```

```objc
- (void) visitRemoveMemberFromGroupEvent:(CNChangeHistoryRemoveMemberFromGroupEvent *) event;
```

## Discussion

Inspect the group and contact in the event that the system provides and update your app’s cached data accordingly.

## Parameters

- `event`: The event object that represents a user removing a contact from a group.

## See Also

### Updating contacts in groups
- [func visitAddMember(CNChangeHistoryAddMemberToGroupEvent)](./visitaddmember%28_%29.md)
  Tells the delegate that the user added a contact to a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visitremovemember(_:))*