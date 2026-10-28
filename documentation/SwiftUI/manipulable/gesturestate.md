# Manipulable.GestureState

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Describes the state of a manipulation gesture.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct GestureState
```

## Overview

> **See Also**: [`manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)`](../view/manipulationgesture%28updating,coordinatespace,operations,inertia,isenabled,onchanged%29.md)

> **See Also**: [`manipulable(using:)`](../view/manipulable%28using%29.md)

## Topics

### Initializers
- [init(transform: AffineTransform3D)](./gesturestate/init%28transform%29.md)
  Creates a new manipulation gesture state with the given transform.
### Instance Properties
- [var isActive: Bool](./gesturestate/isactive.md)
  The Boolean value that indicates whether a manipulation gesture is currently active.
- [var transform: AffineTransform3D](./gesturestate/transform.md)
  The current 3D affine transform applied by an active manipulation gesture.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulable/gesturestate)*