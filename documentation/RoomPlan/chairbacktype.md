# ChairBackType

**Framework**: RoomPlan  
**Kind**: enum

Types of chair back the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ChairBackType
```

#### Overview

When the framework observes a chair in the physical environment during a scan, it chooses a type among these options that best matches the look of the chair’s back. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the chair in the captured room.

## Topics

### Choosing a chair back type
- [ChairBackType.existing](chairbacktype/existing.md)
  A type of chair that has a back.
- [ChairBackType.missing](chairbacktype/missing.md)
  A type of chair that has no back.

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

- [enum ChairType](chairtype.md)
  Types of chair that the framework identifies in a captured room.
- [enum ChairArmType](chairarmtype.md)
  Types of armchair the framework identifies in a captured room.
- [enum ChairLegType](chairlegtype.md)
  Types of chair legs the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/chairbacktype)*