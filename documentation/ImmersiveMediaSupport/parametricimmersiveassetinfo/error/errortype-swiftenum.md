# ParametricImmersiveAssetInfo.Error.ErrorType

**Framework**: Immersive Media Support  
**Kind**: enum

A type of an error that may occur when converting the original wide field of view video asset to a parametric immersive asset.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ErrorType
```

#### Overview

If an error is thrown, continue playing the original AVAsset.

## Topics

### Enumeration Cases
- [ParametricImmersiveAssetInfo.Error.ErrorType.unsupportedAsset](parametricimmersiveassetinfo/error/errortype-swift.enum/unsupportedasset.md)
  Indicates that the asset can’t be converted due to a currently unsupported camera model or capture mode.
- [ParametricImmersiveAssetInfo.Error.ErrorType.isAlreadyConverted](parametricimmersiveassetinfo/error/errortype-swift.enum/isalreadyconverted.md)
  Indicates that the asset was previously converted to parametric immersive format.
- [ParametricImmersiveAssetInfo.Error.ErrorType.unconvertibleAsset](parametricimmersiveassetinfo/error/errortype-swift.enum/unconvertibleasset.md)
  Indicates that the asset can’t be converted because it’s missing the required metadata.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/error/errortype-swift.enum)*