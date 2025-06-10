# ParametricImmersiveAssetInfo.Error.ErrorType

**Framework**: Immersive Media Support  
**Kind**: enum

ParametricImmersiveAssetInfo error type enum. If any error is thrown, please continue play the original AVAsset as is.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum ErrorType
```

## Topics

### Operators
- [static func == (ParametricImmersiveAssetInfo.Error.ErrorType, ParametricImmersiveAssetInfo.Error.ErrorType) -> Bool](parametricimmersiveassetinfo/error/errortype-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ParametricImmersiveAssetInfo.Error.ErrorType.unsupportedAsset](parametricimmersiveassetinfo/error/errortype-swift.enum/unsupportedasset.md)
  Asset cannot be converted due to currently unsupported camera model or capture mode.
- [ParametricImmersiveAssetInfo.Error.ErrorType.unconvertibleAsset](parametricimmersiveassetinfo/error/errortype-swift.enum/unconvertibleasset.md)
  Asset cannot be converted due to missing required metadata.
### Instance Properties
- [var hashValue: Int](parametricimmersiveassetinfo/error/errortype-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](parametricimmersiveassetinfo/error/errortype-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](parametricimmersiveassetinfo/error/errortype-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/error/errortype-swift.enum)*