# SFSpeechLanguageModel.Configuration

**Framework**: Speech  
**Kind**: class  
**Role**: Class

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

```objc
@interface SFSpeechLanguageModelConfiguration : NSObject
```

#### Overview

Pass this object to [`prepareCustomLanguageModel(for:configuration:completion:)`](./preparecustomlanguagemodel%28for,configuration,completion%29.md) to indicate where that method should create the custom language model file, and to [`customizedLanguageModel`](../sfspeechrecognitionrequest/customizedlanguagemodel.md) or [`customizedLanguage(modelConfiguration:)`](../dictationtranscriber/contenthint/customizedlanguage%28modelconfiguration%29.md) to indicate where the system should find that model to use.

## Topics

### Creating a language model configuration
- [init(languageModel: URL)](./configuration/init%28languagemodel%29.md)
  Creates a configuration with the location of a language model file.
- [init(languageModel: URL, vocabulary: URL?)](./configuration/init%28languagemodel,vocabulary%29.md)
  Creates a configuration with the locations of language model and vocabulary files.
- [init(languageModel: URL, vocabulary: URL?, weight: NSNumber?)](./configuration/init%28languagemodel,vocabulary,weight%29.md)
  Creates a configuration with the locations of language model and vocabulary files, and custom weight.
### Inspecting a language model
- [var languageModel: URL](./configuration/languagemodel.md)
  The location of a compiled language model file.
- [var vocabulary: URL?](./configuration/vocabulary.md)
  The location of a compiled vocabulary file.
- [var weight: NSNumber?](./configuration/weight.md)
  The relative weight of the language model customization. Value must be between 0.0 and 1.0 inclusive.
### Initializers
- [init?(coder: NSCoder)](./configuration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Custom vocabulary
- [class AnalysisContext](../analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFSpeechLanguageModel](../sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [class SFCustomLanguageModelData](../sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration)*