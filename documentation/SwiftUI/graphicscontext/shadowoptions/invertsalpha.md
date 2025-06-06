# invertsAlpha

**Framework**: SwiftUI  
**Kind**: property

An option that causes the filter to invert the alpha of the shadow.

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
static var invertsAlpha: GraphicsContext.ShadowOptions { get }
```

#### Discussion

You can create an “inner shadow” effect by combining this option with [`shadowAbove`](graphicscontext/shadowoptions/shadowabove.md) and using the [`sourceAtop`](graphicscontext/blendmode-swift.struct/sourceatop.md) blend mode.

## See Also

- [static var disablesGroup: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/disablesgroup.md)
  An option that causes the filter to composite the object and its shadow separately in the current layer.
- [static var shadowAbove: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/shadowabove.md)
  An option that causes the filter to draw the shadow above the object, rather than below it.
- [static var shadowOnly: GraphicsContext.ShadowOptions](graphicscontext/shadowoptions/shadowonly.md)
  An option that causes the filter to draw only the shadow, and omit the source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shadowoptions/invertsalpha)*