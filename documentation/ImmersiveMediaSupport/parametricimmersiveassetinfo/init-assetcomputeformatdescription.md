# init(asset:computeFormatDescription:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an instance using the passed asset and computes the format description for converting the asset to parametric immersive asset, if requested. Use `ParametricImmersiveAssetInfo.isParametricImmersive` to check whether the asset is already parametric immersive.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(asset: AVURLAsset, computeFormatDescription: Bool = true) async throws
```

## Parameters

- `asset`: The original `AVURLAsset`.
- `computeFormatDescription`: A flag that indicates whether to run the calculation for converting the `ParametricImmersive` asset. Opt-out for a quick check if the content is convertible, result is stored in isAssetConvertible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/init(asset:computeformatdescription:))*