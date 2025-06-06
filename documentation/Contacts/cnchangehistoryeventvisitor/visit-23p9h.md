# visit(_:)

**Framework**: Contacts  
**Kind**: method

Tells the delegate that the user updated a group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func visit(_ event: CNChangeHistoryUpdateGroupEvent)
```

#### Discussion

Inspect the group in the event that the system provides and update your app’s cached data accordingly.

## Parameters

- `event`: The event object that represents a user updating a group.

## See Also

- [func visit(CNChangeHistoryAddGroupEvent)](cnchangehistoryeventvisitor/visit(_:)-ve62.md)
  Tells the delegate that the user added a group.
- [func visit(CNChangeHistoryDeleteGroupEvent)](cnchangehistoryeventvisitor/visit(_:)-82duo.md)
  Tells the delegate that the user deleted a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visit(_:)-23p9h)*