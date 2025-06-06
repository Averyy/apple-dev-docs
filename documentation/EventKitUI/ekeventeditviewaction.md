# EKEventEditViewAction

**Framework**: EventKit UI  
**Kind**: enum

The action taken by the user after editing an event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum EKEventEditViewAction
```

## Topics

### Constants
- [EKEventEditViewAction.canceled](ekeventeditviewaction/canceled.md)
  The user canceled changes made to the event.
- [EKEventEditViewAction.saved](ekeventeditviewaction/saved.md)
  The user saved changes made to the event.
- [EKEventEditViewAction.deleted](ekeventeditviewaction/deleted.md)
  The user deleted the event.
- [static var cancelled: EKEventEditViewAction](ekeventeditviewaction/cancelled.md)
  A static variable used to cancel changes made to the event.
### Initializers
- [init?(rawValue: Int)](ekeventeditviewaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func eventEditViewController(EKEventEditViewController, didCompleteWith: EKEventEditViewAction)](ekeventeditviewdelegate/eventeditviewcontroller(_:didcompletewith:).md)
  Invoked when the user finishes editing an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction)*