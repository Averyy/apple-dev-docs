# UIEvent.EventType

**Framework**: UIKit  
**Kind**: enum

Constants that specify the general type of an event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum EventType
```

#### Overview

You can obtain the type of an event from the [`type`](uievent/type.md) property. To further identify the event, you might also need to determine its subtype, which you obtain from the [`subtype`](uievent/subtype.md) property.

## Topics

### Constants
- [UIEvent.EventType.touches](uievent/eventtype/touches.md)
  The event relates to touches on the screen.
- [UIEvent.EventType.motion](uievent/eventtype/motion.md)
  The event relates to motion of the device, such as when a person shakes it.
- [UIEvent.EventType.remoteControl](uievent/eventtype/remotecontrol.md)
  The event is a remote-control event.
- [UIEvent.EventType.presses](uievent/eventtype/presses.md)
  The event relates to the press of a physical button.
- [UIEvent.EventType.scroll](uievent/eventtype/scroll.md)
  The event relates to scrolling from an indirect input device.
- [UIEvent.EventType.hover](uievent/eventtype/hover.md)
  The event relates to a pointer from an indirect input device moving over a user interface element.
- [UIEvent.EventType.transform](uievent/eventtype/transform.md)
  The event relates to a pointer from an indirect input device performing a transformation on a user interface element, such as scaling, rotation, or translation.
### Initializers
- [init?(rawValue: Int)](uievent/eventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: UIEvent.EventType](uievent/type.md)
  Returns the type of the event.
- [var subtype: UIEvent.EventSubtype](uievent/subtype.md)
  Returns the subtype of the event.
- [UIEvent.EventSubtype](uievent/eventsubtype.md)
  Constants that specify the subtype of the event in relation to its general type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/eventtype)*