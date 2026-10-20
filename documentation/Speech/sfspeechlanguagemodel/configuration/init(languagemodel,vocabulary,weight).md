# init(languageModel:vocabulary:weight:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates a configuration with the locations of language model and vocabulary files, and custom weight.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(languageModel: URL, vocabulary: URL?, weight: NSNumber?)
```

```objc
- (instancetype) initWithLanguageModel:(NSURL *) languageModel vocabulary:(NSURL *) vocabulary weight:(NSNumber *) weight;
```

## See Also

### Creating a language model configuration
- [init(languageModel: URL)](./init%28languagemodel%29.md)
  Creates a configuration with the location of a language model file.
- [init(languageModel: URL, vocabulary: URL?)](./init%28languagemodel,vocabulary%29.md)
  Creates a configuration with the locations of language model and vocabulary files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration/init(languagemodel:vocabulary:weight:))*