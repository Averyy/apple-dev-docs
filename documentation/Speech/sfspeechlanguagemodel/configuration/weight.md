# weight

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The relative weight of the language model customization. Value must be between 0.0 and 1.0 inclusive.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var weight: NSNumber? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * weight;
```

## See Also

### Inspecting a language model
- [var languageModel: URL](./languagemodel.md)
  The location of a compiled language model file.
- [var vocabulary: URL?](./vocabulary.md)
  The location of a compiled vocabulary file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration/weight)*