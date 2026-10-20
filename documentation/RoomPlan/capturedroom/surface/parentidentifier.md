# parentIdentifier

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

A unique alphanumeric value that identifies a surface’s parent surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var parentIdentifier: UUID? { get }
```

#### Discussion

For example, the parent of a window is the wall surface on which the window rests.

## See Also

### Identifying a surface
- [var identifier: UUID](./identifier.md)
  A unique alphanumeric value that the framework assigns the surface.
- [var category: CapturedRoom.Surface.Category](./category-swift.property.md)
  A classification that the captured room assigns the surface.
- [CapturedRoom.Surface.Category](./category-swift.enum.md)
  Classifications of a surface in a captured room.
- [var confidence: CapturedRoom.Confidence](./confidence.md)
  A level of certainty in the surface’s category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/parentidentifier)*