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

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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