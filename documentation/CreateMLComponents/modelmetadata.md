# ModelMetadata

**Framework**: Create ML Components  
**Kind**: struct

User info keys that specify useful information about a model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct ModelMetadata
```

## Topics

### Creating a model
- [init(description: String, version: String, author: String, license: String, creatorDefined: [String : String])](modelmetadata/init(description:version:author:license:creatordefined:).md)
  Creates model metadata.
### Getting the properties
- [var author: String](modelmetadata/author.md)
  The author of this model.
- [var creatorDefined: [String : String]](modelmetadata/creatordefined.md)
  Creator-defined custom metadata.
- [var description: String](modelmetadata/description.md)
  A short description of what the model does and/or its purpose.
- [var license: String](modelmetadata/license.md)
  License information for the model.
- [var version: String](modelmetadata/version.md)
  A version number encoded as a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MLModelTransformerAdaptor](mlmodeltransformeradaptor.md)
  A transformer that uses a Core ML model.
- [struct MLModelClassifierAdaptor](mlmodelclassifieradaptor.md)
  A transformer that uses a Core ML model as a classifier.
- [struct MLModelRegressorAdaptor](mlmodelregressoradaptor.md)
  A transformer that uses a Core ML model as a regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/modelmetadata)*