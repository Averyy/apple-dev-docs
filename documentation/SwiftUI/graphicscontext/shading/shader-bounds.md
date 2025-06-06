# shader(_:bounds:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills with the results of querying a shader for each pixel.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func shader(_ shader: Shader, bounds: CGRect = .zero) -> GraphicsContext.Shading
```

#### Return Value

A shading instance that fills using the shader.

#### Discussion

For a shader function to act as a shape fill it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader, and `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the premultiplied color value in the color space of the destination (typically sRGB).

## Parameters

- `shader`: The shader defining the filled colors.
- `bounds`: The rect used to define any   arguments   of the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/shader(_:bounds:))*