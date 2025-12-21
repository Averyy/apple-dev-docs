# SofaType

**Framework**: RoomPlan  
**Kind**: enum

Types of sofa the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum SofaType
```

#### Overview

When the framework observes a sofa in the physical environment during a scan, it chooses a type among these options that best matches the sofa’s look. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the sofa in the captured room.

## Topics

### Choosing a sofa type
- [SofaType.rectangular](sofatype/rectangular.md)
  A sofa shape that resembles a rectangle.
- [SofaType.singleSeat](sofatype/singleseat.md)
  A sofa that resembles a loveseat.
- [SofaType.lShaped](sofatype/lshaped.md)
  A sofa shape that resembles the letter L.
- [SofaType.lShapedExtension](sofatype/lshapedextension.md)
  The short side of the L-shape sofa.
- [SofaType.unidentified](sofatype/unidentified.md)
  An uncategorized sofa shape.

## Relationships

### Conforms To
- [CapturedRoomAttribute](capturedroomattribute.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/sofatype)*