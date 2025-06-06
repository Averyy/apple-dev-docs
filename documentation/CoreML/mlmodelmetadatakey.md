# MLModelMetadataKey

**Framework**: Core ML  
**Kind**: struct

The set of keys the model uses to store values in its metadata dictionary.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct MLModelMetadataKey
```

## Topics

### Metadata Keys
- [static let author: MLModelMetadataKey](mlmodelmetadatakey/author.md)
  Key for the author of the model.
- [static let description: MLModelMetadataKey](mlmodelmetadatakey/description.md)
  Key for the overall description of the model.
- [static let license: MLModelMetadataKey](mlmodelmetadatakey/license.md)
  Key for the license of the model.
- [static let versionString: MLModelMetadataKey](mlmodelmetadatakey/versionstring.md)
  Key for the version of the model.
- [static let creatorDefinedKey: MLModelMetadataKey](mlmodelmetadatakey/creatordefinedkey.md)
  Key for the model creator’s custom metadata.
### Creating Metadata
- [init(rawValue: String)](mlmodelmetadatakey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var classLabels: [Any]?](mlmodeldescription/classlabels.md)
  An array of labels, which can be either strings or a numbers, for classifier models.
- [var metadata: [MLModelMetadataKey : Any]](mlmodeldescription/metadata.md)
  A dictionary of the model’s creation information, such as its description, author, version, and license.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelmetadatakey)*