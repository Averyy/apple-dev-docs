# identifier

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

A unique alphanumeric value that the framework assigns the surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var identifier: UUID { get }
```

## See Also

### Identifying a surface
- [var parentIdentifier: UUID?](./parentidentifier.md)
  A unique alphanumeric value that identifies a surface’s parent surface.
- [var category: CapturedRoom.Surface.Category](./category-swift.property.md)
  A classification that the captured room assigns the surface.
- [CapturedRoom.Surface.Category](./category-swift.enum.md)
  Classifications of a surface in a captured room.
- [var confidence: CapturedRoom.Confidence](./confidence.md)
  A level of certainty in the surface’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/identifier)*