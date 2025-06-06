# delegate

**Framework**: EventKit UI  
**Kind**: property

The event view controller’s delegate.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any EKEventViewDelegate)? { get set }
```

## See Also

- [protocol EKEventViewDelegate](ekeventviewdelegate.md)
  Delegates used to display details for calendar events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/delegate)*