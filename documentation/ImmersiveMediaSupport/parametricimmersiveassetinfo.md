# ParametricImmersiveAssetInfo

**Framework**: Immersive Media Support  
**Kind**: class

An object that helps convert the original wide field of view video asset to parametric immersive asset.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class ParametricImmersiveAssetInfo
```

## Topics

### Structures
- [ParametricImmersiveAssetInfo.Error](parametricimmersiveassetinfo/error.md)
  ParametricImmersiveAssetInfo error struct.
### Initializers
- [init(asset: AVURLAsset, computeFormatDescription: Bool) async throws](parametricimmersiveassetinfo/init(asset:computeformatdescription:).md)
  Initializes the object with AVURLAsset and compute the CMFormatDescription for converting the asset to ParametricImmersive asset. Use ParametricImmersiveAssetInfo.isParametricImmersive to check if asset is already ParametricImmersive beforehand.
### Instance Properties
- [var isConvertible: Bool?](parametricimmersiveassetinfo/isconvertible.md)
  Result boolean to indicate if the asset can be converted to ParametricImmersive asset or not. If opt-out computeFormatDescription in the init, this boolean shows if asset is potentially convertible.
- [var requiredFormatDescription: CMFormatDescription?](parametricimmersiveassetinfo/requiredformatdescription.md)
  Result CMFormatDescription for overriding on AVMutableMovie video track, which will convert asset to ParametricImmersive asset. Use replaceFormatDescription to replace the format description on the AVMutableMovieTrack.
### Type Methods
- [class func isParametricImmersive(asset: AVURLAsset) async -> Bool](parametricimmersiveassetinfo/isparametricimmersive(asset:).md)
  Checks asynchronously if the asset is already in the ParametricImmersive format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo)*