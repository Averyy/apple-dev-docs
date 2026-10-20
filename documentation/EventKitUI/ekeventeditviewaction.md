# EKEventEditViewAction

**Framework**: EventKit UI  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum EKEventEditViewAction : NSInteger;
```

## Topics

### Constants
- [EKEventEditViewAction.canceled](./ekeventeditviewaction/canceled.md)
  The user canceled changes made to the event.
- [EKEventEditViewAction.saved](./ekeventeditviewaction/saved.md)
  The user saved changes made to the event.
- [EKEventEditViewAction.deleted](./ekeventeditviewaction/deleted.md)
  The user deleted the event.
- [static var cancelled: EKEventEditViewAction](./ekeventeditviewaction/cancelled.md)
  A static variable used to cancel changes made to the event.
### Initializers
- [init?(rawValue: Int)](./ekeventeditviewaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Finishing an Edit
- [func eventEditViewController(EKEventEditViewController, didCompleteWith: EKEventEditViewAction)](./ekeventeditviewdelegate/eventeditviewcontroller%28_,didcompletewith%29.md)
  Invoked when the user finishes editing an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction)*