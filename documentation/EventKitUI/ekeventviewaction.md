# EKEventViewAction

**Framework**: EventKit UI  
**Kind**: enum

Describes the action taken to close the event view controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum EKEventViewAction
```

## Topics

### Constants
- [EKEventViewAction.done](ekeventviewaction/done.md)
  The user tapped the Done button.
- [EKEventViewAction.responded](ekeventviewaction/responded.md)
  The user responded to and saved a pending event invitation.
- [EKEventViewAction.deleted](ekeventviewaction/deleted.md)
  The user deleted the event.
### Initializers
- [init?(rawValue: Int)](ekeventviewaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func eventViewController(EKEventViewController, didCompleteWith: EKEventViewAction)](ekeventviewdelegate/eventviewcontroller(_:didcompletewith:).md)
  Invoked when closing the event view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewaction)*