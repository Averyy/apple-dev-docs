# colorShader(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that applies `shader` to the color of each source pixel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func colorShader(_ shader: Shader) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies the shader  as a color filter.

#### Discussion

For a shader function to act as a color filter it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, half4 color, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader and `color` its source color, as a pre-multiplied color in the destination color space. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the modified color value.

## Parameters

- `shader`: The shader to apply to   as a color filter.

## See Also

- [static func distortionShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](graphicscontext/filter/distortionshader(_:maxsampleoffset:).md)
  Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.
- [static func layerShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](graphicscontext/filter/layershader(_:maxsampleoffset:).md)
  Returns a filter that applies `shader` to the contents of the source layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colorshader(_:))*