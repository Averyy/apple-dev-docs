# SFSpeechLanguageModel

**Framework**: Speech  
**Kind**: class

A language model built from custom training data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechLanguageModel
```

#### Overview

Create this object using [`prepareCustomLanguageModel(for:configuration:completion:)`](sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:completion:).md) or [`prepareCustomLanguageModel(for:configuration:ignoresCache:completion:)`](sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:ignorescache:completion:).md).

## Topics

### Type Methods
- [class func prepareCustomLanguageModel(for: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, completion: ((any Error)?) -> Void)](sfspeechlanguagemodel/preparecustomlanguagemodel(for:clientidentifier:configuration:completion:).md)
- [class func prepareCustomLanguageModel(for: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool, completion: ((any Error)?) -> Void)](sfspeechlanguagemodel/preparecustomlanguagemodel(for:clientidentifier:configuration:ignorescache:completion:).md)
- [class func prepareCustomLanguageModel(for: URL, configuration: SFSpeechLanguageModel.Configuration, completion: ((any Error)?) -> Void)](sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:completion:).md)
  Creates a language model from custom training data.
- [class func prepareCustomLanguageModel(for: URL, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool, completion: ((any Error)?) -> Void)](sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:ignorescache:completion:).md)
  Creates a language model from custom training data.
### Classes
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AnalysisContext](analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [protocol DataInsertable](datainsertable.md)
  A protocol supporting the custom language model training data result builder.
- [protocol TemplateInsertable](templateinsertable.md)
  A protocol supporting the custom language model training data result builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel)*