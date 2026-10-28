# DockAccessory.Animation

**Framework**: DockKit  
**Kind**: enum  
**Role**: Enumeration

Character animations that describe how to move the dock accessory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum Animation
```

## Overview

Each animation executes on a predefined trajectory. See [`animate(motion:)`](./animate%28motion%29.md) for more information.

## Topics

### Enumeration Cases
- [DockAccessory.Animation.kapow](./animation/kapow.md)
  The dock accessory performs a quick tilt and snaps back with some oscillation.
- [DockAccessory.Animation.no](./animation/no.md)
  The dock accessory traces a horizontal head shake.
- [DockAccessory.Animation.wakeup](./animation/wakeup.md)
  The dock accessory moves upwards towards center.
- [DockAccessory.Animation.yes](./animation/yes.md)
  The dock accessory traces a vertical head nod.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing animation
- [func animate(motion: DockAccessory.Animation) async throws -> Progress](./animate%28motion%29.md)
  Starts an animation sequence.
- [func setRegionOfInterest(CGRect) async throws](./setregionofinterest%28_%29.md)
  Sets the area in the video frame in which the dock accessory tracks a subject.
- [var regionOfInterest: CGRect](./regionofinterest.md)
  The area in the video frame in which the dock accessory tracks a subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/animation)*