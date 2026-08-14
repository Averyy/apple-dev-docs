# BreakthroughEffect

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct BreakthroughEffect
```

## Topics

### Type Properties
- [static let automatic: BreakthroughEffect](breakthrougheffect/automatic.md)
  The system will choose the best effect for the type of element and its position within the scene. This might result in no breakthrough effect.
- [static let none: BreakthroughEffect](breakthrougheffect/none.md)
  The element is clipped by occluding content. This is not supported when used to customize a sheet breakthrough effect.
- [static let prominent: BreakthroughEffect](breakthrougheffect/prominent.md)
  The element is prominently revealed through occluding content.
- [static let subtle: BreakthroughEffect](breakthrougheffect/subtle.md)
  The element is subtly blended over occluding content.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](view/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [struct SurroundingsEffect](surroundingseffect.md)
  Effects that the system can apply to passthrough video.
- [func breakthroughEffect(BreakthroughEffect) -> some View](view/breakthrougheffect(_:).md)
  Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/breakthrougheffect)*