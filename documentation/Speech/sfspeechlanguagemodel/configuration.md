# SFSpeechLanguageModel.Configuration

**Framework**: Speech  
**Kind**: class

An object describing the location of a custom language model and specialized vocabulary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class Configuration
```

#### Overview

Pass this object to [`prepareCustomLanguageModel(for:configuration:completion:)`](sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:completion:).md) to indicate where that method should create the custom language model file, and to [`customizedLanguageModel`](sfspeechrecognitionrequest/customizedlanguagemodel.md) or [`customizedLanguage(modelConfiguration:)`](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md) to indicate where the system should find that model to use.

## Topics

### Initializers
- [init(languageModel: URL)](sfspeechlanguagemodel/configuration/init(languagemodel:).md)
  Creates a configuration with the location of a language model file.
- [init(languageModel: URL, vocabulary: URL?)](sfspeechlanguagemodel/configuration/init(languagemodel:vocabulary:).md)
  Creates a configuration with the locations of language model and vocabulary files.
- [init(languageModel: URL, vocabulary: URL?, weight: NSNumber?)](sfspeechlanguagemodel/configuration/init(languagemodel:vocabulary:weight:).md)
  Creates a configuration with the locations of language model and vocabulary files, and custom weight.
### Instance Properties
- [var languageModel: URL](sfspeechlanguagemodel/configuration/languagemodel.md)
  The location of a compiled language model file.
- [var vocabulary: URL?](sfspeechlanguagemodel/configuration/vocabulary.md)
  The location of a compiled vocabulary file.
- [var weight: NSNumber?](sfspeechlanguagemodel/configuration/weight.md)
  The relative weight of the language model customization. Value must be between 0.0 and 1.0 inclusive.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AnalysisContext](analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [protocol DataInsertable](datainsertable.md)
  A protocol supporting the custom language model training data result builder.
- [protocol TemplateInsertable](templateinsertable.md)
  A protocol supporting the custom language model training data result builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration)*