# luminanceToAlpha

**Framework**: SwiftUI  
**Kind**: property

Returns a filter that sets the opacity of each pixel based on its luminance.

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
static var luminanceToAlpha: GraphicsContext.Filter { get }
```

#### Return Value

A filter that applies a luminance to alpha transformation.

#### Discussion

The filter computes the luminance of each pixel and uses it to define the opacity of the result, combined with black (zero) color components.

## See Also

- [static func alphaThreshold(min: Double, max: Double, color: Color) -> GraphicsContext.Filter](graphicscontext/filter/alphathreshold(min:max:color:).md)
  Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/luminancetoalpha)*