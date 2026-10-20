# init(url:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates a speech recognition request, initialized with the specified URL.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL;
```

#### Discussion

Use this method to create a request to recognize speech in a recorded audio file that resides at the specified URL. Pass the request to the recognizer’s [`recognitionTask(with:delegate:)`](../sfspeechrecognizer/recognitiontask%28with,delegate%29.md) method to start recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechurlrecognitionrequest/init(url:)-3ymmz)*