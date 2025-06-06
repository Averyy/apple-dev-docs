# visit(_:)

**Framework**: Contacts  
**Kind**: method  
**Required**: Yes

Tells the delegate to drop all contacts and groups before handling more events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func visit(_ event: CNChangeHistoryDropEverythingEvent)
```

#### Discussion

When the system sends this event to your delegate, enough has changed since the last time your app fetched the history changes that an incremental update is no longer possible. Following the drop everything event, the system sends your delegate an add event for each contact and group currently in the database. This allows you to implement full syncs and incremental syncs using the same code.

## Parameters

- `event`: The event that indicates the delegate should drop all contacts and groups before handling more events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor/visit(_:)-2yhz3)*