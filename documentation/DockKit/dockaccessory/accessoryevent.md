# DockAccessory.AccessoryEvent

**Framework**: DockKit  
**Kind**: enum

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

### Operators
- [static func == (DockAccessory.AccessoryEvent, DockAccessory.AccessoryEvent) -> Bool](dockaccessory/accessoryevent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [DockAccessory.AccessoryEvent.button(id:pressed:)](dockaccessory/accessoryevent/button(id:pressed:).md)
  A button press event on the dock accessory.
- [DockAccessory.AccessoryEvent.cameraFlip](dockaccessory/accessoryevent/cameraflip.md)
  A camera flip event that indicates a request to switch between back and front cameras.
- [DockAccessory.AccessoryEvent.cameraShutter](dockaccessory/accessoryevent/camerashutter.md)
  A camera shutter toggle event.
- [DockAccessory.AccessoryEvent.cameraZoom(factor:)](dockaccessory/accessoryevent/camerazoom(factor:).md)
  A camera zoom event.
### Instance Properties
- [var hashValue: Int](dockaccessory/accessoryevent/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/accessoryevent/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/accessoryevent/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/accessoryevent)*