# clipBoundingRect

**Framework**: SwiftUI  
**Kind**: property

The bounding rectangle of the intersection of all current clip shapes in the current user space.

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
var clipBoundingRect: CGRect { get }
```

## See Also

- [func clip(to: Path, style: FillStyle, options: GraphicsContext.ClipOptions)](graphicscontext/clip(to:style:options:).md)
  Adds a path to the context’s array of clip shapes.
- [func clipToLayer(opacity: Double, options: GraphicsContext.ClipOptions, content: (inout GraphicsContext) throws -> Void) rethrows](graphicscontext/cliptolayer(opacity:options:content:).md)
  Adds a clip shape that you define in a new layer to the context’s array of clip shapes.
- [GraphicsContext.ClipOptions](graphicscontext/clipoptions.md)
  Options that affect the use of clip shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/clipboundingrect)*