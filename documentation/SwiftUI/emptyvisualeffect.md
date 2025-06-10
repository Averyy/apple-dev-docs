# EmptyVisualEffect

**Framework**: SwiftUI  
**Kind**: struct

The base visual effect that you apply additional effect to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct EmptyVisualEffect
```

#### Overview

`EmptyVisualEffect` does not change the appearance of the view that it is applied to.

## Topics

### Creating an empty visual effect
- [init()](emptyvisualeffect/init.md)
  Creates a new empty visual effect.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisualEffect](visualeffect.md)

## See Also

- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](view/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](view/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [protocol VisualEffect](visualeffect.md)
  Visual Effects change the visual appearance of a view without changing its ancestors or descendents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptyvisualeffect)*