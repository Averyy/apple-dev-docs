# bestTranscription

**Framework**: Speech  
**Kind**: property

The transcription with the highest confidence level.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var bestTranscription: SFTranscription { get }
```

## See Also

- [var transcriptions: [SFTranscription]](sfspeechrecognitionresult/transcriptions.md)
  An array of potential transcriptions, sorted in descending order of confidence.
- [var speechRecognitionMetadata: SFSpeechRecognitionMetadata?](sfspeechrecognitionresult/speechrecognitionmetadata.md)
  An object that contains the metadata results for a speech recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionresult/besttranscription)*