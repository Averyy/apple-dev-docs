# UIDragInteraction

**Framework**: UIKit  
**Kind**: class

An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDragInteraction
```

## Mentions

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

## Topics

### Initializing the drag interaction
- [init(delegate: any UIDragInteractionDelegate)](uidraginteraction/init(delegate:).md)
  Initializes a drag interaction object with a custom delegate object.
### Managing drag interactions
- [var allowsSimultaneousRecognitionDuringLift: Bool](uidraginteraction/allowssimultaneousrecognitionduringlift.md)
  A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.
- [var delegate: (any UIDragInteractionDelegate)?](uidraginteraction/delegate.md)
  An object that configures and controls a drag interaction.
- [protocol UIDragInteractionDelegate](uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.
### Enabling the interactions
- [var isEnabled: Bool](uidraginteraction/isenabled.md)
  A Boolean value that specifies whether the drag interaction responds to touches and is allowed to participate in a drag activity.
- [class var isEnabledByDefault: Bool](uidraginteraction/isenabledbydefault.md)
  A device-dependent Boolean value that indicates whether a newly-instantiated drag interaction is allowed to participate in a drag activity.

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
- [class UIDropInteraction](uidropinteraction.md)
  An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction)*