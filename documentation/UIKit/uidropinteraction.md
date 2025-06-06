# UIDropInteraction

**Framework**: UIKit  
**Kind**: class

An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDropInteraction
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

## Topics

### Initializing drop interactions
- [init(delegate: any UIDropInteractionDelegate)](uidropinteraction/init(delegate:).md)
  Initializes a drop interaction object with a custom delegate object.
### Managing drop interactions
- [var delegate: (any UIDropInteractionDelegate)?](uidropinteraction/delegate.md)
  An object that configures and controls a drop interaction.
- [protocol UIDropInteractionDelegate](uidropinteractiondelegate.md)
  The interface for configuring and controlling a drop interaction.
### Allowing simultaneous drops
- [var allowsSimultaneousDropSessions: Bool](uidropinteraction/allowssimultaneousdropsessions.md)
  A Boolean value that specifies whether the drop interaction handles more than one simultaneous drop session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UIDragInteractionDelegate](uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.
- [protocol UIDropInteractionDelegate](uidropinteractiondelegate.md)
  The interface for configuring and controlling a drop interaction.
- [class UIDragInteraction](uidraginteraction.md)
  An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteraction)*