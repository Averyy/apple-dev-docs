# TableType

**Framework**: RoomPlan  
**Kind**: enum

Types of table the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum TableType
```

#### Overview

When the framework observes a table in the physical environment during a scan, it chooses a type among these options that best matches the table’s look. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the table in the captured room.

## Topics

### Choosing a chair type
- [TableType.dining](tabletype/dining.md)
  A table top for the purpose of dining.
- [TableType.coffee](tabletype/coffee.md)
  A table top that resembles a coffee table.
- [TableType.unidentified](tabletype/unidentified.md)
  An uncategorized table top.

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

## See Also

- [enum TableShapeType](tableshapetype.md)
  Different table shapes that the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/tabletype)*