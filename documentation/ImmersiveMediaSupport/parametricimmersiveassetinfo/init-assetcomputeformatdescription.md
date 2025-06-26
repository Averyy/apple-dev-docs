# init(asset:computeFormatDescription:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes the object with `AVURLAsset` and compute the `CMFormatDescription` for converting the asset to parametric immersive asset. Use `ParametricImmersiveAssetInfo.isParametricImmersive` to check if the asset is already parametric immersive or not beforehand.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(asset: AVURLAsset, computeFormatDescription: Bool = true) async throws
```

## Parameters

- `asset`: Original AVURLAsset.
- `computeFormatDescription`: Flag to indicate if will run the calculation for converting the ParametricImmersive. Opt-out for a quick check if the content is convertible, result is stored in isAssetConvertible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/init(asset:computeformatdescription:))*