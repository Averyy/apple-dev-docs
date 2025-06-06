# distortionShader(_:maxSampleOffset:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func distortionShader(_ shader: Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter
```

#### Return Value

A new filter that applies the shader as a distortion effect.

#### Discussion

For a shader function to act as a distortion effect it must have a function signature matching:

```swift
[[ stitchable ]] float2 name(float2 position, args...)
```

where `position` is the user-space coordinates of the destination pixel applied to the shader. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the user-space coordinates of the corresponding source pixel.

## Parameters

- `shader`: The shader to apply as a distortion effect.
- `maxSampleOffset`: The maximum distance in each axis   between the returned source pixel position and the   destination pixel position, for all source pixels.

## See Also

- [static func colorShader(Shader) -> GraphicsContext.Filter](graphicscontext/filter/colorshader(_:).md)
  Returns a filter that applies `shader` to the color of each source pixel.
- [static func layerShader(Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter](graphicscontext/filter/layershader(_:maxsampleoffset:).md)
  Returns a filter that applies `shader` to the contents of the source layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/distortionshader(_:maxsampleoffset:))*