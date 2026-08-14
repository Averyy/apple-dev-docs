# TableShapeType

**Framework**: RoomPlan  
**Kind**: enum

Different table shapes that the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum TableShapeType
```

#### Overview

When the framework observes a table in the physical environment during a scan, it chooses a type among these options that best matches the table’s shape. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the table in the captured room.

## Topics

### Choosing a chair type
- [TableShapeType.rectangular](tableshapetype/rectangular.md)
  A table shape that resembles a rectangle.
- [TableShapeType.circularElliptic](tableshapetype/circularelliptic.md)
  A table shape that resembles an ellipse.
- [TableShapeType.lShaped](tableshapetype/lshaped.md)
  A table shape that resembles the letter L.
- [TableShapeType.unidentified](tableshapetype/unidentified.md)
  An uncategorized table shape.

## Relationships

### Conforms To
- [CapturedRoomAttribute](capturedroomattribute.md)
- [CaseIterable](../swift/caseiterable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum TableType](tabletype.md)
  Types of table the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/tableshapetype)*