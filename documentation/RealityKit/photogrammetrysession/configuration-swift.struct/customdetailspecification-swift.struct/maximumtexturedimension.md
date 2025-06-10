# maximumTextureDimension

**Framework**: RealityKit  
**Kind**: property

The maximum dimension of the reconstructed texture maps.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var maximumTextureDimension: PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureDimension
```

#### Discussion

The reconstructed texture map will have width and height dimensions both less than or equal to the provided `maxTextureDimension`. This property is useful for fitting within the texture memory resources of the rendering system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct/maximumtexturedimension)*