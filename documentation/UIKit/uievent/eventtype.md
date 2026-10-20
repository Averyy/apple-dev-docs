# UIEvent.EventType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the general type of an event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum EventType
```

```c
enum UIEventType : NSInteger;
```

#### Overview

You can obtain the type of an event from the [`type`](./type.md) property. To further identify the event, you might also need to determine its subtype, which you obtain from the [`subtype`](./subtype.md) property.

## Topics

### Constants
- [UIEvent.EventType.touches](./eventtype/touches.md)
  The event relates to touches on the screen.
- [UIEvent.EventType.motion](./eventtype/motion.md)
  The event relates to motion of the device, such as when a person shakes it.
- [UIEvent.EventType.remoteControl](./eventtype/remotecontrol.md)
  The event is a remote-control event.
- [UIEvent.EventType.presses](./eventtype/presses.md)
  The event relates to the press of a physical button.
- [UIEvent.EventType.scroll](./eventtype/scroll.md)
  The event relates to scrolling from an indirect input device.
- [UIEvent.EventType.hover](./eventtype/hover.md)
  The event relates to a pointer from an indirect input device moving over a user interface element.
- [UIEvent.EventType.transform](./eventtype/transform.md)
  The event relates to a pointer from an indirect input device performing a transformation on a user interface element, such as scaling, rotation, or translation.
### Initializers
- [init?(rawValue: Int)](./eventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the event type
- [var type: UIEvent.EventType](./type.md)
  Returns the type of the event.
- [var subtype: UIEvent.EventSubtype](./subtype.md)
  Returns the subtype of the event.
- [UIEvent.EventSubtype](./eventsubtype.md)
  Constants that specify the subtype of the event in relation to its general type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/eventtype)*