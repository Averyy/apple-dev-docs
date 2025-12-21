# prepareCustomLanguageModel(for:configuration:ignoresCache:completion:)

**Framework**: Speech  
**Kind**: method

Creates a language model from custom training data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func prepareCustomLanguageModel(for asset: URL, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool) async throws
```

## Parameters

- `asset`: The URL of a file containing custom training data. Create this file with  .
- `configuration`: An object listing the URLs at which this method should create the language model and compiled vocabulary from the training data.
- `ignoresCache`: If  , the language model identified by the configuration will be recreated even if the   file is unchanged.
- `completion`: Called when the language model has been created.

## See Also

- [class func prepareCustomLanguageModel(for: URL, configuration: SFSpeechLanguageModel.Configuration, completion: ((any Error)?) -> Void)](sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:completion:).md)
  Creates a language model from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:ignorescache:completion:))*