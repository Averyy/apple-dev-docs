# EKEventViewAction

**Framework**: EventKit UI  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum EKEventViewAction : NSInteger;
```

## Topics

### Constants
- [EKEventViewAction.done](./ekeventviewaction/done.md)
  The user tapped the Done button.
- [EKEventViewAction.responded](./ekeventviewaction/responded.md)
  The user responded to and saved a pending event invitation.
- [EKEventViewAction.deleted](./ekeventviewaction/deleted.md)
  The user deleted the event.
### Initializers
- [init?(rawValue: Int)](./ekeventviewaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to the Interface’s Dismissal
- [func eventViewController(EKEventViewController, didCompleteWith: EKEventViewAction)](./ekeventviewdelegate/eventviewcontroller%28_,didcompletewith%29.md)
  Invoked when closing the event view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewaction)*