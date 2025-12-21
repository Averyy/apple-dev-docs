# MLModelMetadata

**Framework**: Create ML  
**Kind**: struct

Information about a model that’s stored in a Core ML model file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLModelMetadata
```

## Mentions

- [Creating a text classifier model](creating-a-text-classifier-model.md)
- [Creating a word tagger model](creating-a-word-tagger-model.md)

#### Overview

Create a metadata instance and store it as part of your model when you export a Core ML model. You can examine this metadata in Xcode when you import the model into your app.

## Topics

### Creating metadata
- [init(author: String, shortDescription: String, license: String?, version: String, additional: [String : String]?)](mlmodelmetadata/init(author:shortdescription:license:version:additional:).md)
  Creates a new metadata instance for a machine learning model.
### Accessing metadata
- [var author: String](mlmodelmetadata/author.md)
  The author of the model.
- [var shortDescription: String](mlmodelmetadata/shortdescription.md)
  A short text description of the model.
- [var license: String?](mlmodelmetadata/license.md)
  The license governing the use of the model.
- [var version: String](mlmodelmetadata/version.md)
  The model version.
- [var additional: [String : String]?](mlmodelmetadata/additional.md)
  A dictionary that encodes key value pairs to hold additional information about the model.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MLCreateError](mlcreateerror.md)
  The errors Create ML throws while performing various operations, such as training models, making predictions, writing models to a file system, and so on.
- [enum MLSplitStrategy](mlsplitstrategy.md)
  Data partitioning approaches, typically for creating a validation dataset from a training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlmodelmetadata)*