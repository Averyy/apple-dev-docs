# ChairType

**Framework**: RoomPlan  
**Kind**: enum

Types of chair that the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ChairType
```

#### Overview

When the framework observes a chair in the physical environment during a scan, it chooses a type among these options that best matches the chair’s look. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the chair in the captured room.

## Topics

### Choosing a chair type
- [ChairType.dining](chairtype/dining.md)
  A type of chair that accompanies a dining table.
- [ChairType.stool](chairtype/stool.md)
  A type of chair that resembles a stool.
- [ChairType.swivel](chairtype/swivel.md)
  A type of chair that swivels.
- [ChairType.unidentified](chairtype/unidentified.md)
  An uncategorized chair type.

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

- [enum ChairArmType](chairarmtype.md)
  Types of armchair the framework identifies in a captured room.
- [enum ChairLegType](chairlegtype.md)
  Types of chair legs the framework identifies in a captured room.
- [enum ChairBackType](chairbacktype.md)
  Types of chair back the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/chairtype)*