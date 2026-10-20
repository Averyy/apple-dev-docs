# AssetError.Kind

**Framework**: Core AI  
**Kind**: enum  
**Role**: Enumeration

The reasons an asset operation can fail.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Kind
```

## Topics

### Types of errors
- [AssetError.Kind.corruptedMetadata](./kind-swift.enum/corruptedmetadata.md)
  An error that indicates the asset metadata is corrupted.
- [AssetError.Kind.duplicateName](./kind-swift.enum/duplicatename.md)
  An error that indicates a component with that name already exists in the asset.
- [AssetError.Kind.invalidFeatureType(_:)](./kind-swift.enum/invalidfeaturetype%28_%29.md)
  An error that indicates the feature type is invalid.
- [AssetError.Kind.invalidName](./kind-swift.enum/invalidname.md)
  An error that indicates the component name is invalid.
- [AssetError.Kind.unsupportedVersion(_:)](./kind-swift.enum/unsupportedversion%28_%29.md)
  An error that indicates the asset version is unsupported.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/asseterror/kind-swift.enum)*