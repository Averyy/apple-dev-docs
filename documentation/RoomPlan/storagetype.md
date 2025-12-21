# StorageType

**Framework**: RoomPlan  
**Kind**: enum

Types of storage area that the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum StorageType
```

#### Overview

When the framework observes a storage area in the physical environment, it chooses a type among these options that best matches the type of storage. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) in the captured room that represents the storage in the captured room.

## Topics

### Choosing a storage area type
- [StorageType.cabinet](storagetype/cabinet.md)
  An enclosed storage area.
- [StorageType.shelf](storagetype/shelf.md)
  An open, wall-located storage area.

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

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/storagetype)*