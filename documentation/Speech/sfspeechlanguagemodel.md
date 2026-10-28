# SFSpeechLanguageModel

**Framework**: Speech  
**Kind**: class  
**Role**: Class

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

```objc
@interface SFSpeechLanguageModel : NSObject
```

## Overview

Create this object using [`prepareCustomLanguageModel(for:configuration:completion:)`](./sfspeechlanguagemodel/preparecustomlanguagemodel%28for,configuration,completion%29.md) or [`prepareCustomLanguageModel(for:configuration:ignoresCache:completion:)`](./sfspeechlanguagemodel/preparecustomlanguagemodel%28for,configuration,ignorescache,completion%29.md).

## Topics

### Creating a custom language model
- [class func prepareCustomLanguageModel(for: URL, configuration: SFSpeechLanguageModel.Configuration, completion: ((any Error)?) -> Void)](./sfspeechlanguagemodel/preparecustomlanguagemodel%28for,configuration,completion%29.md)
  Creates a language model from custom training data.
- [class func prepareCustomLanguageModel(for: URL, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool, completion: ((any Error)?) -> Void)](./sfspeechlanguagemodel/preparecustomlanguagemodel%28for,configuration,ignorescache,completion%29.md)
  Creates a language model from custom training data.
- [SFSpeechLanguageModel.Configuration](./sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
### Type Methods
- [class func prepareCustomLanguageModel(for: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, completion: ((any Error)?) -> Void)](./sfspeechlanguagemodel/preparecustomlanguagemodel%28for,clientidentifier,configuration,completion%29.md)
- [class func prepareCustomLanguageModel(for: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool, completion: ((any Error)?) -> Void)](./sfspeechlanguagemodel/preparecustomlanguagemodel%28for,clientidentifier,configuration,ignorescache,completion%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom vocabulary
- [class AnalysisContext](./analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [SFSpeechLanguageModel.Configuration](./sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [class SFCustomLanguageModelData](./sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel)*