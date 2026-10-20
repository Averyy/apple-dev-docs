# NLModel.ModelType

**Framework**: Natural Language  
**Kind**: enum  
**Role**: Enumeration

The different types of a natural language model.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum ModelType
```

```c
enum NLModelType : NSInteger;
```

## Topics

### Model types
- [NLModel.ModelType.sequence](./modeltype/sequence.md)
  A sequence model type that tags text at the token level.
- [NLModel.ModelType.classifier](./modeltype/classifier.md)
  A classifier model type that tags text at the phrase, sentence, paragraph, or higher level.
### Initializers
- [init?(rawValue: Int)](./modeltype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the configuration
- [var language: NLLanguage?](../nlmodelconfiguration/language.md)
  The language the model supports.
- [var revision: Int](../nlmodelconfiguration/revision.md)
  The version of the Natural Language framework that trained the model.
- [class func supportedRevisions(for: NLModel.ModelType) -> IndexSet](../nlmodelconfiguration/supportedrevisions%28for%29.md)
  Returns the versions of the Natural Language framework the OS supports.
- [class func currentRevision(for: NLModel.ModelType) -> Int](../nlmodelconfiguration/currentrevision%28for%29.md)
  Returns the current Natural Language framework version in the OS.
- [var type: NLModel.ModelType](../nlmodelconfiguration/type.md)
  The natural language model type of the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/modeltype)*