# AssetError.Kind.invalidFeatureType(_:)

**Framework**: Core AI  
**Kind**: case  
**Role**: Case

An error that indicates the feature type is invalid.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case invalidFeatureType(String)
```

#### Discussion

This means that either the feature type has an incorrect name, or that the asset comes from a more recent version of the library and you may need to upgrade.

## See Also

### Types of errors
- [AssetError.Kind.corruptedMetadata](./corruptedmetadata.md)
  An error that indicates the asset metadata is corrupted.
- [AssetError.Kind.duplicateName](./duplicatename.md)
  An error that indicates a component with that name already exists in the asset.
- [AssetError.Kind.invalidName](./invalidname.md)
  An error that indicates the component name is invalid.
- [AssetError.Kind.unsupportedVersion(_:)](./unsupportedversion%28_%29.md)
  An error that indicates the asset version is unsupported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/asseterror/kind-swift.enum/invalidfeaturetype(_:))*