# ParametricImmersiveAssetInfo

**Framework**: Immersive Media Support  
**Kind**: class

An object that helps convert the original wide field of view video asset to parametric immersive asset.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class ParametricImmersiveAssetInfo
```

## Topics

### Structures
- [ParametricImmersiveAssetInfo.Error](parametricimmersiveassetinfo/error.md)
  An error that occurs during the conversion process of the parametric immersive asset.
### Initializers
- [init(asset: AVURLAsset, computeFormatDescription: Bool) async throws](parametricimmersiveassetinfo/init(asset:computeformatdescription:).md)
  Creates an instance using the passed asset and computes the format description for converting the asset to parametric immersive asset, if requested. Use `ParametricImmersiveAssetInfo.isParametricImmersive` to check whether the asset is already parametric immersive.
### Instance Properties
- [var requiredFormatDescription: CMFormatDescription?](parametricimmersiveassetinfo/requiredformatdescription.md)
  A result format descriptor for overriding a mutable video track that’s used to convert the asset to parametric immersive asset. Use `replaceFormatDescription` to replace the format description on the `AVMutableMovieTrack`.
- [var conversionResult: Result<CMFormatDescription, ParametricImmersiveAssetInfo.Error>?](parametricimmersiveassetinfo/conversionresult.md)
  The result object of the parametric immersive format conversion.
- [var isAssetConvertible: Bool](parametricimmersiveassetinfo/isassetconvertible.md)
  A result Boolean value that indicates whether the asset can be converted to parametric immersive. If opt-out `computeFormatDescription` in the initializer, this Boolean indicates whether the asset is convertible.
### Type Methods
- [class func isParametricImmersive(asset: AVURLAsset) async -> Bool](parametricimmersiveassetinfo/isparametricimmersive(asset:).md)
  Checks asynchronously whether the asset is already in the parametric immersive format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo)*