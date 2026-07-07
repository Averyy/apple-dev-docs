# AssetError.Kind.invalidFeatureType(_:)

**Framework**: Core AI  
**Kind**: case

An error that indicates the feature type is invalid.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case invalidFeatureType(String)
```

#### Discussion

This means that either the feature type has an incorrect name, or that the asset comes from a more recent version of the library and you may need to upgrade.

## See Also

- [AssetError.Kind.corruptedMetadata](asseterror/kind-swift.enum/corruptedmetadata.md)
  An error that indicates the asset metadata is corrupted.
- [AssetError.Kind.duplicateName](asseterror/kind-swift.enum/duplicatename.md)
  An error that indicates a component with that name already exists in the asset.
- [AssetError.Kind.invalidName](asseterror/kind-swift.enum/invalidname.md)
  An error that indicates the component name is invalid.
- [AssetError.Kind.unsupportedVersion(_:)](asseterror/kind-swift.enum/unsupportedversion(_:).md)
  An error that indicates the asset version is unsupported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/asseterror/kind-swift.enum/invalidfeaturetype(_:))*