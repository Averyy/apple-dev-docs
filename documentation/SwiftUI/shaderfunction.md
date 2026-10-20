# ShaderFunction

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A reference to a function in a Metal shader library.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@dynamicCallable
struct ShaderFunction
```

## Topics

### Creating a shader function
- [init(library: ShaderLibrary, name: String)](./shaderfunction/init%28library,name%29.md)
  Creates a new function reference from the provided shader library and function name string.
### Configuring a function
- [var library: ShaderLibrary](./shaderfunction/library.md)
  The shader library storing the function.
- [var name: String](./shaderfunction/name.md)
  The name of the shader function in the library.
- [func dynamicallyCall(withArguments: [Shader.Argument]) -> Shader](./shaderfunction/dynamicallycall%28witharguments%29.md)
  Returns a new shader by applying the provided argument values to the referenced function.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Metal shaders
- [func colorEffect(Shader, isEnabled: Bool) -> some View](./view/coloreffect%28_,isenabled%29.md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](./view/distortioneffect%28_,maxsampleoffset,isenabled%29.md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](./view/layereffect%28_,maxsampleoffset,isenabled%29.md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [struct Shader](./shader.md)
  A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [struct ShaderLibrary](./shaderlibrary.md)
  A Metal shader library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shaderfunction)*