# speechRecognitionMetadata

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

An object that contains the metadata results for a speech recognition request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var speechRecognitionMetadata: SFSpeechRecognitionMetadata? { get }
```

```objc
@property (nonatomic, readonly, nullable) SFSpeechRecognitionMetadata * speechRecognitionMetadata;
```

## See Also

### Getting transcriptions
- [var bestTranscription: SFTranscription](./besttranscription.md)
  The transcription with the highest confidence level.
- [var transcriptions: [SFTranscription]](./transcriptions.md)
  An array of potential transcriptions, sorted in descending order of confidence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionresult/speechrecognitionmetadata)*