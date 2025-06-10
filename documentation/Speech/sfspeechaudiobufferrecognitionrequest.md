# SFSpeechAudioBufferRecognitionRequest

**Framework**: Speech  
**Kind**: class

A request to recognize speech from captured audio content, such as audio from the device’s microphone.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechAudioBufferRecognitionRequest
```

#### Overview

Use an [`SFSpeechAudioBufferRecognitionRequest`](sfspeechaudiobufferrecognitionrequest.md) object to perform speech recognition on live audio, or on a set of existing audio buffers. For example, use this request object to route audio from a device’s microphone to the speech recognizer.

The request object contains no audio initially. As you capture audio, call [`append(_:)`](sfspeechaudiobufferrecognitionrequest/append(_:).md) or [`appendAudioSampleBuffer(_:)`](sfspeechaudiobufferrecognitionrequest/appendaudiosamplebuffer(_:).md) to add audio samples to the request object. The speech recognizer continuously analyzes the audio you appended, stopping only when you call the [`endAudio()`](sfspeechaudiobufferrecognitionrequest/endaudio().md) method. You must call [`endAudio()`](sfspeechaudiobufferrecognitionrequest/endaudio().md) explicitly to stop the speech recognition process.

For a complete example of how to use audio buffers with speech recognition, see [`SpeakToMe: Using Speech Recognition with AVAudioEngine`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/SpeakToMe/Introduction/Intro.html#//apple_ref/doc/uid/TP40017110).

## Topics

### Appending Audio Buffers
- [func append(AVAudioPCMBuffer)](sfspeechaudiobufferrecognitionrequest/append(_:).md)
  Appends audio in the PCM format to the end of the recognition request.
- [func appendAudioSampleBuffer(CMSampleBuffer)](sfspeechaudiobufferrecognitionrequest/appendaudiosamplebuffer(_:).md)
  Appends audio to the end of the recognition request.
- [func endAudio()](sfspeechaudiobufferrecognitionrequest/endaudio.md)
  Marks the end of audio input for the recognition request.
### Getting the Audio Format
- [var nativeAudioFormat: AVAudioFormat](sfspeechaudiobufferrecognitionrequest/nativeaudioformat.md)
  The preferred audio format for optimal speech recognition.

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
- [class SFSpeechURLRecognitionRequest](sfspeechurlrecognitionrequest.md)
  A request to recognize speech in a recorded audio file.
- [class SFSpeechRecognitionRequest](sfspeechrecognitionrequest.md)
  An abstract class that represents a request to recognize speech from an audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechaudiobufferrecognitionrequest)*