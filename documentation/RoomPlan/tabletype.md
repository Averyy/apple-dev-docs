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
### Identifying a chair type
- [var shortIdentifier: String](tabletype/shortidentifier.md)
  A human-readable identifier for the attribute.
### Categorizing a chair type
- [static var parentCategory: CapturedElementCategory?](tabletype/parentcategory.md)
  A category to which this room attribute belongs.
### Creating a chair type
- [init?(rawValue: String)](tabletype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](tabletype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [TableType.AllCases](tabletype/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [TableType.RawValue](tabletype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [TableType]](tabletype/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](tabletype/equatable-implementations.md)
- [RawRepresentable Implementations](tabletype/rawrepresentable-implementations.md)

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