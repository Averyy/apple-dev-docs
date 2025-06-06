# CapturedRoom.Surface.Category

**Framework**: RoomPlan  
**Kind**: enum

Classifications of a surface in a captured room.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Category
```

#### Overview

Each [`CapturedRoom.Surface`](capturedroom/surface.md) instance in a captured room’s surface arrays ([`doors`](capturedroom/doors.md), [`openings`](capturedroom/openings.md), [`walls`](capturedroom/walls.md), and [`windows`](capturedroom/windows.md)) reflects a classification ([`category`](capturedroom/surface/category-swift.property.md)) of this type.

## Topics

### Creating a surface category
- [init(from: any Decoder) throws](capturedroom/surface/category-swift.enum/init(from:).md)
  Creates a surface category by deserializing the specified decoder.
### Determining the surface category
- [CapturedRoom.Surface.Category.floor](capturedroom/surface/category-swift.enum/floor.md)
  A category for a surface that represents a floor.
- [CapturedRoom.Surface.Category.door(isOpen:)](capturedroom/surface/category-swift.enum/door(isopen:).md)
  A category for a surface that represents a door.
- [CapturedRoom.Surface.Category.opening](capturedroom/surface/category-swift.enum/opening.md)
  A category for a surface that represents an opening.
- [CapturedRoom.Surface.Category.wall](capturedroom/surface/category-swift.enum/wall.md)
  A category for a surface that represents a wall.
- [CapturedRoom.Surface.Category.window](capturedroom/surface/category-swift.enum/window.md)
  A category for a surface that represents a window.
### Serializing a surface category
- [func encode(to: any Encoder) throws](capturedroom/surface/category-swift.enum/encode(to:).md)
  Serializes a surface category to the specified encoder.
### Comparing surface categories
- [static func == (CapturedRoom.Surface.Category, CapturedRoom.Surface.Category) -> Bool](capturedroom/surface/category-swift.enum/==(_:_:).md)
  Determines whether two surface categories are equal.
- [static func != (Self, Self) -> Bool](capturedroom/surface/category-swift.enum/!=(_:_:).md)
  Determines whether two surface categories aren’t equal.
- [var hashValue: Int](capturedroom/surface/category-swift.enum/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](capturedroom/surface/category-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](capturedroom/surface/category-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var identifier: UUID](capturedroom/surface/identifier.md)
  A unique alphanumeric value that the framework assigns the surface.
- [var parentIdentifier: UUID?](capturedroom/surface/parentidentifier.md)
  A unique alphanumeric value that identifies a surface’s parent surface.
- [var category: CapturedRoom.Surface.Category](capturedroom/surface/category-swift.property.md)
  A classification that the captured room assigns the surface.
- [var confidence: CapturedRoom.Confidence](capturedroom/surface/confidence.md)
  A level of certainty in the surface’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/category-swift.enum)*