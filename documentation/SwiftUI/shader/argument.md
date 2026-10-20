# Shader.Argument

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A single uniform argument value to a shader function.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Argument
```

## Topics

### Creating argument values
- [static var boundingRect: Shader.Argument](./argument/boundingrect.md)
  Returns an argument value representing the bounding rect of the shape or view that the shader is attached to, as `float4(x, y, width, height)`. This value is undefined for shaders that do not have a natural bounding rect (e.g. filter effects drawn into `GraphicsContext`).
- [static func color(Color) -> Shader.Argument](./argument/color%28_%29.md)
  Returns an argument value representing `color`. When passed to a MSL function it will convert to a `half4` value, as a premultiplied color in the target color space.
- [static func colorArray([Color]) -> Shader.Argument](./argument/colorarray%28_%29.md)
  Returns an argument value defined by the provided array of color values. When passed to an MSL function it will convert to a `device const half4 *ptr, int count` pair of parameters.
- [static func data(Data) -> Shader.Argument](./argument/data%28_%29.md)
  Returns an argument value defined by the provided data value. When passed to an MSL function it will convert to a `device const void *ptr, int size_in_bytes` pair of parameters.
- [static func float<T>(T) -> Shader.Argument](./argument/float%28_%29.md)
  Returns an argument value representing the MSL value `float(x)`.
- [static float2(_:)](./argument/float2%28_%29.md)
  Returns an argument value representing the MSL value `float2(point.x, point.y)`.
- [static func float2<T>(T, T) -> Shader.Argument](./argument/float2%28_,_%29.md)
  Returns an argument value representing the MSL value `float2(x, y)`.
- [static func float3<T>(T, T, T) -> Shader.Argument](./argument/float3%28_,_,_%29.md)
  Returns an argument value representing the MSL value `float3(x, y, z)`.
- [static func float4<T>(T, T, T, T) -> Shader.Argument](./argument/float4%28_,_,_,_%29.md)
  Returns an argument value representing the MSL value `float4(x, y, z, w)`.
- [static func floatArray([Float]) -> Shader.Argument](./argument/floatarray%28_%29.md)
  Returns an argument value defined by the provided array of floating point numbers. When passed to an MSL function it will convert to a `device const float *ptr, int count` pair of parameters.
- [static func image(Image) -> Shader.Argument](./argument/image%28_%29.md)
  Returns an argument value defined by the provided image. When passed to an MSL function it will convert to a `texture2d<half>` value. Currently only one image parameter is supported per `Shader` instance.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a shader
- [init(function: ShaderFunction, arguments: [Shader.Argument])](./init%28function,arguments%29.md)
  Creates a new shader from a function and the uniform argument values to bind to the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shader/argument)*