# SFSpeechURLRecognitionRequest

**Framework**: Speech  
**Kind**: class

A request to recognize speech in a recorded audio file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechURLRecognitionRequest
```

#### Overview

Use this object to perform speech recognition on the contents of an audio file.

The following example shows a method that performs recognition on an audio file based on the user’s default language and prints out the transcription.

Listing 1. Getting a speech recognizer and making a recognition request

```swift
func recognizeFile(url: URL) {
    // Create a speech recognizer associated with the user's default language.
    guard let myRecognizer = SFSpeechRecognizer() else {
        // The system doesn't support the user's default language.
        return
    }
    
    guard myRecognizer.isAvailable else {
        // The recognizer isn't available.
        return
    }
    
    // Create and execute a speech recognition request for the audio file at the URL.
    let request = SFSpeechURLRecognitionRequest(url: url)
    myRecognizer.recognitionTask(with: request) { (result, error) in
        guard let result else {
            // Recognition failed, so check the error for details and handle it.
            return
        }
        
        // Print the speech transcription with the highest confidence that the
        // system recognized.
        if result.isFinal {
            print(result.bestTranscription.formattedString)
        }
    }
}
```

## Topics

### Creating a Speech Recognition Request
- [init(url: URL)](sfspeechurlrecognitionrequest/init(url:).md)
  Creates a speech recognition request, initialized with the specified URL.
### Accessing the URL of the Audio File
- [var url: URL](sfspeechurlrecognitionrequest/url.md)
  The URL of the audio file.

## Relationships

### Inherits From
- [SFSpeechRecognitionRequest](sfspeechrecognitionrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Recognizing speech in live audio](recognizing-speech-in-live-audio.md)
  Perform speech recognition on audio coming from the microphone of an iOS device.
- [class SFSpeechAudioBufferRecognitionRequest](sfspeechaudiobufferrecognitionrequest.md)
  A request to recognize speech from captured audio content, such as audio from the device’s microphone.
- [class SFSpeechRecognitionRequest](sfspeechrecognitionrequest.md)
  An abstract class that represents a request to recognize speech from an audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechurlrecognitionrequest)*