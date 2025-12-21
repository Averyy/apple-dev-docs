# Manipulable.GestureState

**Framework**: SwiftUI  
**Kind**: struct

Describes the state of a manipulation gesture.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct GestureState
```

#### Overview

> **Note**: [`manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)`](view/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:).md)

> **Note**: [`manipulable(using:)`](view/manipulable(using:).md)

## Topics

### Initializers
- [init(transform: AffineTransform3D)](manipulable/gesturestate/init(transform:).md)
  Creates a new manipulation gesture state with the given transform.
### Instance Properties
- [var isActive: Bool](manipulable/gesturestate/isactive.md)
  The Boolean value that indicates whether a manipulation gesture is currently active.
- [var transform: AffineTransform3D](manipulable/gesturestate/transform.md)
  The current 3D affine transform applied by an active manipulation gesture.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulable/gesturestate)*