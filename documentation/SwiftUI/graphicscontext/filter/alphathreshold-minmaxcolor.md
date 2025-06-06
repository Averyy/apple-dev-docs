# alphaThreshold(min:max:color:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.

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
static func alphaThreshold(min: Double, max: Double = 1, color: Color = Color.black) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies a threshold to alpha values.

## Parameters

- `min`: The minimum alpha threshold. Pixels whose alpha   component is less than this value will render as   transparent. Results are undefined unless  .
- `max`: The maximum alpha threshold. Pixels whose alpha   component is greater than this value will render   as transparent. Results are undefined unless  .
- `color`: The color that is output for pixels with an alpha   component between the two threshold values.

## See Also

- [static var luminanceToAlpha: GraphicsContext.Filter](graphicscontext/filter/luminancetoalpha.md)
  Returns a filter that sets the opacity of each pixel based on its luminance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/alphathreshold(min:max:color:))*