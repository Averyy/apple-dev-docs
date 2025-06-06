# colorEffect(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func colorEffect(_ shader: Shader, isEnabled: Bool = true) -> some View
```

#### Return Value

A new view that renders `self` with the shader applied as a color filter.

#### Discussion

For a shader function to act as a color filter it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, half4 color, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader and `color` its source color, as a pre-multiplied color in the destination color space. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the modified color value.

> ❗ **Important**: Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## Parameters

- `shader`: The shader to apply to   as a color filter.
- `isEnabled`: Whether the effect is enabled or not.

## See Also

- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [struct Shader](shader.md)
  A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [struct ShaderFunction](shaderfunction.md)
  A reference to a function in a Metal shader library.
- [struct ShaderLibrary](shaderlibrary.md)
  A Metal shader library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/coloreffect(_:isenabled:))*