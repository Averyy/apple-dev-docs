# visit(_:)

**Framework**: Contacts  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user updated a contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func visit(_ event: CNChangeHistoryUpdateContactEvent)
```

#### Discussion

Inspect the contact in the event that the system provides and update your app’s cached data accordingly.

## Parameters

- `event`: The event object that represents a user updating a contact.

## See Also

- [func visit(CNChangeHistoryAddContactEvent)](cnchangehistoryeventvisitor/visit(_:)-9w73y.md)
  Tells the delegate that the user added a contact.
- [func visit(CNChangeHistoryDeleteContactEvent)](cnchangehistoryeventvisitor/visit(_:)-ci4z.md)
  Tells the delegate that the user deleted a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visit(_:)-1pf2a)*