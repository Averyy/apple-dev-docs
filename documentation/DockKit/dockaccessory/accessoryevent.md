# DockAccessory.AccessoryEvent

**Framework**: DockKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents an accessory event.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
enum AccessoryEvent
```

#### Overview

This event propagates input from the dock accessory. Example events are button presses or requests for common camera controls.

## Topics

### Enumeration Cases
- [DockAccessory.AccessoryEvent.button(id:pressed:)](./accessoryevent/button%28id,pressed%29.md)
  A button press event on the dock accessory.
- [DockAccessory.AccessoryEvent.cameraFlip](./accessoryevent/cameraflip.md)
  A camera flip event that indicates a request to switch between back and front cameras.
- [DockAccessory.AccessoryEvent.cameraShutter](./accessoryevent/camerashutter.md)
  A camera shutter toggle event.
- [DockAccessory.AccessoryEvent.cameraZoom(factor:)](./accessoryevent/camerazoom%28factor%29.md)
  A camera zoom event.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/accessoryevent)*