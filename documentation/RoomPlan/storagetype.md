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
### Identifying a storage area type
- [var shortIdentifier: String](storagetype/shortidentifier.md)
  A human-readable identifier for the attribute.
### Categorizing a storage area type
- [static var parentCategory: CapturedElementCategory?](storagetype/parentcategory.md)
  A category to which this room attribute belongs.
### Creating a storage area type
- [init?(rawValue: String)](storagetype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](storagetype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [StorageType.AllCases](storagetype/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [StorageType.RawValue](storagetype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [StorageType]](storagetype/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](storagetype/equatable-implementations.md)
- [RawRepresentable Implementations](storagetype/rawrepresentable-implementations.md)

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