# CapturedRoom.Object.Category

**Framework**: RoomPlan  
**Kind**: enum

Classifications of an object in a captured room.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Category
```

#### Overview

Each [`CapturedRoom.Object`](capturedroom/object.md) instance in a captured room’s [`objects`](capturedroom/objects.md) array reflects a classification ([`category`](capturedroom/object/category-swift.property.md)) of this type.

## Topics

### Creating an object category
- [init(from: any Decoder) throws](capturedroom/object/category-swift.enum/init(from:).md)
  Creates an object category by deserializing the specified decoder.
### Determining the object category
- [CapturedRoom.Object.Category.bathtub](capturedroom/object/category-swift.enum/bathtub.md)
  A category for an object that represents a bathtub.
- [CapturedRoom.Object.Category.bed](capturedroom/object/category-swift.enum/bed.md)
  A category for an object that represents a bed.
- [CapturedRoom.Object.Category.chair](capturedroom/object/category-swift.enum/chair.md)
  A category for an object that represents a chair.
- [CapturedRoom.Object.Category.dishwasher](capturedroom/object/category-swift.enum/dishwasher.md)
  A category for an object that represents a dishwasher.
- [CapturedRoom.Object.Category.fireplace](capturedroom/object/category-swift.enum/fireplace.md)
  A category for an object that represents a fireplace.
- [CapturedRoom.Object.Category.oven](capturedroom/object/category-swift.enum/oven.md)
  A category for an object that represents an oven.
- [CapturedRoom.Object.Category.refrigerator](capturedroom/object/category-swift.enum/refrigerator.md)
  A category for an object that represents a refrigerator.
- [CapturedRoom.Object.Category.sink](capturedroom/object/category-swift.enum/sink.md)
  A category for an object that represents a sink.
- [CapturedRoom.Object.Category.sofa](capturedroom/object/category-swift.enum/sofa.md)
  A category for an object that represents a sofa.
- [CapturedRoom.Object.Category.stairs](capturedroom/object/category-swift.enum/stairs.md)
  A category for an object that represents stairs.
- [CapturedRoom.Object.Category.storage](capturedroom/object/category-swift.enum/storage.md)
  A category for an object that represents a storage area.
- [CapturedRoom.Object.Category.stove](capturedroom/object/category-swift.enum/stove.md)
  A category for an object that represents a stove.
- [CapturedRoom.Object.Category.table](capturedroom/object/category-swift.enum/table.md)
  A category for an object that represents a table.
- [CapturedRoom.Object.Category.television](capturedroom/object/category-swift.enum/television.md)
  A category for an object that represents a television.
- [CapturedRoom.Object.Category.toilet](capturedroom/object/category-swift.enum/toilet.md)
  A category for an object that represents a toilet.
- [CapturedRoom.Object.Category.washerDryer](capturedroom/object/category-swift.enum/washerdryer.md)
  A category for an object that represents a clothes washer or dryer.
### Determining supported attributes
- [var supportedAttributeTypes: [any CapturedRoomAttribute.Type]](capturedroom/object/category-swift.enum/supportedattributetypes.md)
  Defines the attributes types compatible with a particular object category.
- [var supportedCombinations: [[any CapturedRoomAttribute]]](capturedroom/object/category-swift.enum/supportedcombinations.md)
  An array of supported attributes that differs by category.
- [func supportsCombination([any CapturedRoomAttribute]) -> Bool](capturedroom/object/category-swift.enum/supportscombination(_:).md)
  Returns a Boolean value that indicates whether a category supports the given attribute combination.
### Serializing an object category
- [func encode(to: any Encoder) throws](capturedroom/object/category-swift.enum/encode(to:).md)
  Serializes an object category to the specified encoder.
### Comparing object categories
- [static func == (CapturedRoom.Object.Category, CapturedRoom.Object.Category) -> Bool](capturedroom/object/category-swift.enum/==(_:_:).md)
  Determines whether two object categories are equal.
- [static func != (Self, Self) -> Bool](capturedroom/object/category-swift.enum/!=(_:_:).md)
  Determines whether two object categories aren’t equal.
- [var hashValue: Int](capturedroom/object/category-swift.enum/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](capturedroom/object/category-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [CapturedRoom.Object.Category.AllCases](capturedroom/object/category-swift.enum/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [CapturedRoom.Object.Category]](capturedroom/object/category-swift.enum/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](capturedroom/object/category-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var identifier: UUID](capturedroom/object/identifier.md)
  A unique alphanumeric value that the framework assigns the object.
- [var parentIdentifier: UUID?](capturedroom/object/parentidentifier.md)
  A unique alphanumeric value that identifies the object’s parent object or surface.
- [var category: CapturedRoom.Object.Category](capturedroom/object/category-swift.property.md)
  A classification that the captured room assigns the object.
- [var confidence: CapturedRoom.Confidence](capturedroom/object/confidence.md)
  A level of certainty in the object’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object/category-swift.enum)*