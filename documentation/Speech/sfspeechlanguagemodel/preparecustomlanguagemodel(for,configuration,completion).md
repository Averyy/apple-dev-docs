# prepareCustomLanguageModel(for:configuration:completion:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Creates a language model from custom training data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func prepareCustomLanguageModel(for asset: URL, configuration: SFSpeechLanguageModel.Configuration, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
class func prepareCustomLanguageModel(for asset: URL, configuration: SFSpeechLanguageModel.Configuration) async throws
```

```objc
+ (void) prepareCustomLanguageModelForUrl:(NSURL *) asset configuration:(SFSpeechLanguageModelConfiguration *) configuration completion:(void (^)(NSError *error)) completion;
```

## Parameters

- `asset`: The URL of a file containing custom training data. Create this file with [`export(to:)`](../sfcustomlanguagemodeldata/export%28to%29.md).
- `configuration`: An object listing the URLs at which this method should create the language model and compiled vocabulary from the training data.
- `completion`: Called when the language model has been created.

## See Also

### Creating a custom language model
- [class func prepareCustomLanguageModel(for: URL, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool, completion: ((any Error)?) -> Void)](./preparecustomlanguagemodel%28for,configuration,ignorescache,completion%29.md)
  Creates a language model from custom training data.
- [SFSpeechLanguageModel.Configuration](./configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/preparecustomlanguagemodel(for:configuration:completion:))*