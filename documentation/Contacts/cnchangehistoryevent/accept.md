# accept(_:)

**Framework**: Contacts  
**Kind**: method

Forwards the event to the delegate you provide to process the change-history event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func accept(_ visitor: any CNChangeHistoryEventVisitor)
```

## Parameters

- `visitor`: The delegate with methods you implement to handle this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryevent/accept(_:))*