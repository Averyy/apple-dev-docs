# addsPunctuation

**Framework**: Speech  
**Kind**: property

A Boolean value that indicates whether to add punctuation to speech recognition results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var addsPunctuation: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) for the speech framework to automatically include punctuation in the recognition results. Punctuation includes a period or question mark at the end of a sentence, and a comma within a sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/addspunctuation)*