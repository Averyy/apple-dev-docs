# ShaderLibrary

**Framework**: SwiftUI  
**Kind**: struct

A Metal shader library.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@dynamicMemberLookup
struct ShaderLibrary
```

## Topics

### Getting the default shader library
- [static let `default`: ShaderLibrary](shaderlibrary/default.md)
  The default shader library of the main (i.e. app) bundle.
- [static func bundle(Bundle) -> ShaderLibrary](shaderlibrary/bundle(_:).md)
  Returns the default shader library of the specified bundle.
### Creating a shader library
- [init(url: URL)](shaderlibrary/init(url:).md)
  Creates a new Metal shader library from the contents of `url`, which must be the location  of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.
- [init(data: Data)](shaderlibrary/init(data:).md)
  Creates a new Metal shader library from `data`, which must be the contents of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.
### Access shader functions
- [static subscript(dynamicMember _: String) -> ShaderFunction](shaderlibrary/subscript(dynamicmember:)-swift.type.subscript.md)
  Returns a new shader function representing the stitchable MSL function called `name` in the default shader library.
### Subscripts
- [subscript(dynamicMember _: String) -> ShaderFunction](shaderlibrary/subscript(dynamicmember:)-swift.subscript.md)
  Returns a new shader function representing the stitchable MSL function in the library called `name`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func colorEffect(Shader, isEnabled: Bool) -> some View](view/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [struct Shader](shader.md)
  A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [struct ShaderFunction](shaderfunction.md)
  A reference to a function in a Metal shader library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shaderlibrary)*