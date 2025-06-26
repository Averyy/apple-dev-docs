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
  An error that occurs during the conversion process of the ParametricImmersive asset.
### Initializers
- [init(asset: AVURLAsset, computeFormatDescription: Bool) async throws](parametricimmersiveassetinfo/init(asset:computeformatdescription:).md)
  Initializes the object with `AVURLAsset` and compute the `CMFormatDescription` for converting the asset to parametric immersive asset. Use `ParametricImmersiveAssetInfo.isParametricImmersive` to check if the asset is already parametric immersive or not beforehand.
### Instance Properties
- [var isConvertible: Bool?](parametricimmersiveassetinfo/isconvertible.md)
  A result Boolean value that indicates whether the asset can be converted to ParametricImmersive or not. If opt-out `computeFormatDescription` in the init, this boolean shows if asset is potentially convertible.
- [var requiredFormatDescription: CMFormatDescription?](parametricimmersiveassetinfo/requiredformatdescription.md)
  A result format description for overriding on AVMutableMovie video track, which will convert asset to ParametricImmersive asset. Use `replaceFormatDescription` to replace the format description on the `AVMutableMovieTrack`.
- [var conversionResult: Result<CMFormatDescription, ParametricImmersiveAssetInfo.Error>?](parametricimmersiveassetinfo/conversionresult.md)
  The Result object of the ParametricImmersive conversion.
- [var isAssetConvertible: Bool](parametricimmersiveassetinfo/isassetconvertible.md)
  A result Boolean value that indicates whether the asset can be converted to ParametricImmersive or not. If opt-out `computeFormatDescription` in the init, this boolean shows if asset is potentially convertible.
### Type Methods
- [class func isParametricImmersive(asset: AVURLAsset) async -> Bool](parametricimmersiveassetinfo/isparametricimmersive(asset:).md)
  Checks asynchronously if the asset is already in the parametric immersive format or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo)*