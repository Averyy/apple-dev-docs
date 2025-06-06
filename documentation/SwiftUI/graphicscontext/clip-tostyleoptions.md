# clip(to:style:options:)

**Framework**: SwiftUI  
**Kind**: method

Adds a path to the context’s array of clip shapes.

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
mutating func clip(to path: Path, style: FillStyle = FillStyle(), options: GraphicsContext.ClipOptions = ClipOptions())
```

#### Discussion

Call this method to add a shape to the array of clip shapes that the context uses to define a clipping mask. Shapes that you add affect only subsequent drawing operations.

## Parameters

- `path`: A   that defines the shape of the clipping mask.
- `style`: A   that defines how to rasterize the shape.
- `options`: Clip options that tell SwiftUI how to interpret the    as a clip shape. For example, you can invert the clip   shape by setting the   option.

## See Also

- [func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions, content: (inout GraphicsContext) throws -> Void) rethrows](graphicscontext/cliptolayer(opacity:options:content:).md)
  Adds a clip shape that you define in a new layer to the context’s array of clip shapes.
- [var clipBoundingRect: CGRect](graphicscontext/clipboundingrect.md)
  The bounding rectangle of the intersection of all current clip shapes in the current user space.
- [GraphicsContext.ClipOptions](graphicscontext/clipoptions.md)
  Options that affect the use of clip shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/clip(to:style:options:))*