# DockAccessory.Animation

**Framework**: DockKit  
**Kind**: enum

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

#### Overview

Each animation executes on a predefined trajectory. See [`animate(motion:)`](dockaccessory/animate(motion:).md) for more information.

## Topics

### Operators
- [static func == (DockAccessory.Animation, DockAccessory.Animation) -> Bool](dockaccessory/animation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [DockAccessory.Animation.kapow](dockaccessory/animation/kapow.md)
  The dock accessory performs a quick tilt and snaps back with some oscillation.
- [DockAccessory.Animation.no](dockaccessory/animation/no.md)
  The dock accessory traces a horizontal head shake.
- [DockAccessory.Animation.wakeup](dockaccessory/animation/wakeup.md)
  The dock accessory moves upwards towards center.
- [DockAccessory.Animation.yes](dockaccessory/animation/yes.md)
  The dock accessory traces a vertical head nod.
### Instance Properties
- [var hashValue: Int](dockaccessory/animation/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/animation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/animation/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func animate(motion: DockAccessory.Animation) async throws -> Progress](dockaccessory/animate(motion:).md)
  Starts an animation sequence.
- [func setRegionOfInterest(CGRect) async throws](dockaccessory/setregionofinterest(_:).md)
  Sets the area in the video frame in which the dock accessory tracks a subject.
- [var regionOfInterest: CGRect](dockaccessory/regionofinterest.md)
  The area in the video frame in which the dock accessory tracks a subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/animation)*