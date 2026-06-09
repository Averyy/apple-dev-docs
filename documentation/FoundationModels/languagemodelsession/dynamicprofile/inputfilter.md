# inputFilter(_:)

**Framework**: Foundation Models  
**Kind**: method

Apply a transformation to the transcript prior to invoking the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func inputFilter(_ filter: @escaping ([Transcript.Entry]) -> [Transcript.Entry]) -> some LanguageModelSession.DynamicProfile
```

## See Also

- [func historyTransform(([Transcript.Entry]) -> [Transcript.Entry]) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/historytransform(_:).md)
  Apply a transformation to the history prior to invoking the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/inputfilter(_:))*