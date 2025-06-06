# GraphicsContext.ClipOptions

**Framework**: SwiftUI  
**Kind**: struct

Options that affect the use of clip shapes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
struct ClipOptions
```

#### Overview

Use these options to affect how SwiftUI interprets a clip shape when you call [`clip(to:style:options:)`](graphicscontext/clip(to:style:options:).md) to add a path to the array of clip shapes, or when you call [`clipToLayer(opacity:options:content:)`](graphicscontext/cliptolayer(opacity:options:content:).md) to add a clipping layer.

## Topics

### Getting clip options
- [static var inverse: GraphicsContext.ClipOptions](graphicscontext/clipoptions/inverse.md)
  An option to invert the shape or layer alpha as the clip mask.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func clip(to: Path, style: FillStyle, options: GraphicsContext.ClipOptions)](graphicscontext/clip(to:style:options:).md)
  Adds a path to the context’s array of clip shapes.
- [func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions, content: (inout GraphicsContext) throws -> Void) rethrows](graphicscontext/cliptolayer(opacity:options:content:).md)
  Adds a clip shape that you define in a new layer to the context’s array of clip shapes.
- [var clipBoundingRect: CGRect](graphicscontext/clipboundingrect.md)
  The bounding rectangle of the intersection of all current clip shapes in the current user space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/clipoptions)*