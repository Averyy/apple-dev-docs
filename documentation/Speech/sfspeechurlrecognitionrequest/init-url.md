# init(url:)

**Framework**: Speech  
**Kind**: init

Creates a speech recognition request, initialized with the specified URL.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL)
```

#### Discussion

Use this method to create a request to recognize speech in a recorded audio file that resides at the specified URL. Pass the request to the recognizer’s [`recognitionTask(with:delegate:)`](sfspeechrecognizer/recognitiontask(with:delegate:).md) method to start recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechurlrecognitionrequest/init(url:))*