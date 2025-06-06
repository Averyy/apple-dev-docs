# colorDodge

**Framework**: SwiftUI  
**Kind**: property

A mode that brightens the background image samples to reflect the source image samples.

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
static var colorDodge: GraphicsContext.BlendMode { get }
```

#### Discussion

Source image sample values that specify black do not produce a change.

## See Also

- [static var lighten: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/lighten.md)
  A mode that creates composite image samples by choosing the lighter samples from either the source image or the background.
- [static var screen: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/screen.md)
  A mode that multiplies the inverse of the source image samples with the inverse of the background image samples.
- [static var plusLighter: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/pluslighter.md)
  A mode that adds the components of the source and background images, resulting in a lightened composite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/colordodge)*