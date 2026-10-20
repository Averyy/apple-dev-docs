# languageModel

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The location of a compiled language model file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var languageModel: URL { get }
```

```objc
@property (nonatomic, copy, readonly) NSURL * languageModel;
```

## See Also

### Inspecting a language model
- [var vocabulary: URL?](./vocabulary.md)
  The location of a compiled vocabulary file.
- [var weight: NSNumber?](./weight.md)
  The relative weight of the language model customization. Value must be between 0.0 and 1.0 inclusive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration/languagemodel)*