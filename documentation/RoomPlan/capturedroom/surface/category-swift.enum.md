# CapturedRoom.Surface.Category

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

Classifications of a surface in a captured room.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Category
```

## Overview

Each [`CapturedRoom.Surface`](../surface.md) instance in a captured room’s surface arrays ([`doors`](../doors.md), [`openings`](../openings.md), [`walls`](../walls.md), and [`windows`](../windows.md)) reflects a classification ([`category`](./category-swift.property.md)) of this type.

## Topics

### Determining the surface category
- [CapturedRoom.Surface.Category.floor](./category-swift.enum/floor.md)
  A category for a surface that represents a floor.
- [CapturedRoom.Surface.Category.door(isOpen:)](./category-swift.enum/door%28isopen%29.md)
  A category for a surface that represents a door.
- [CapturedRoom.Surface.Category.opening](./category-swift.enum/opening.md)
  A category for a surface that represents an opening.
- [CapturedRoom.Surface.Category.wall](./category-swift.enum/wall.md)
  A category for a surface that represents a wall.
- [CapturedRoom.Surface.Category.window](./category-swift.enum/window.md)
  A category for a surface that represents a window.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Identifying a surface
- [var identifier: UUID](./identifier.md)
  A unique alphanumeric value that the framework assigns the surface.
- [var parentIdentifier: UUID?](./parentidentifier.md)
  A unique alphanumeric value that identifies a surface’s parent surface.
- [var category: CapturedRoom.Surface.Category](./category-swift.property.md)
  A classification that the captured room assigns the surface.
- [var confidence: CapturedRoom.Confidence](./confidence.md)
  A level of certainty in the surface’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/category-swift.enum)*