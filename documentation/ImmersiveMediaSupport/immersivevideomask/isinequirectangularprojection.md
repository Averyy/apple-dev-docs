# isInEquirectangularProjection

**Framework**: Immersive Media Support  
**Kind**: property

A Boolean value that indicates whether the generated mask texture is in equirectangular projection space or not. If this Boolean is true, then the app renderer needs to transform vertices of the mesh to equirectangular projection space to generate UVs to access the mask texture.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var isInEquirectangularProjection: Bool { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask/isinequirectangularprojection)*