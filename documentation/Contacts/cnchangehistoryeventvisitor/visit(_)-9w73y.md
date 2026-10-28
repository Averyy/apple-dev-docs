# visit(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user added a contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func visit(_ event: CNChangeHistoryAddContactEvent)
```

```objc
- (void) visitAddContactEvent:(CNChangeHistoryAddContactEvent *) event;
```

## Discussion

Inspect the contact in the event that the system provides and update your app’s cached data accordingly.

## Parameters

- `event`: The event object that represents a user adding a contact.

## See Also

### Updating contacts
- [func visit(CNChangeHistoryUpdateContactEvent)](./visit%28_%29-1pf2a.md)
  Tells the delegate that the user updated a contact.
- [func visit(CNChangeHistoryDeleteContactEvent)](./visit%28_%29-ci4z.md)
  Tells the delegate that the user deleted a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visit(_:)-9w73y)*