# init(languageModel:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates a configuration with the location of a language model file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(languageModel: URL)
```

```objc
- (instancetype) initWithLanguageModel:(NSURL *) languageModel;
```

## See Also

### Creating a language model configuration
- [init(languageModel: URL, vocabulary: URL?)](./init%28languagemodel,vocabulary%29.md)
  Creates a configuration with the locations of language model and vocabulary files.
- [init(languageModel: URL, vocabulary: URL?, weight: NSNumber?)](./init%28languagemodel,vocabulary,weight%29.md)
  Creates a configuration with the locations of language model and vocabulary files, and custom weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration/init(languagemodel:))*