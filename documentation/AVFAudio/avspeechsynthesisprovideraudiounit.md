# AVSpeechSynthesisProviderAudioUnit

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that generates speech from text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVSpeechSynthesisProviderAudioUnit
```

```objc
@interface AVSpeechSynthesisProviderAudioUnit : AUAudioUnit
```

#### Overview

Use a speech synthesizer audio unit to generate audio buffers that contain speech for a given voice and speech markup. The audio unit receives an [`AVSpeechSynthesisProviderRequest`](./avspeechsynthesisproviderrequest.md) as input, and extracts audio buffers through the render block.

Use [`speechSynthesisOutputMetadataBlock`](./avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md) to provide metadata as an array of [`AVSpeechSynthesisMarker`](./avspeechsynthesismarker.md).

The system scans and loads voices for audio unit extensions of this type, and the voices it provides are available for use in [`AVSpeechSynthesizer`](./avspeechsynthesizer.md) and accessibility technologies like VoiceOver and Speak Screen.

> ❗ **Important**:  Network access isn’t allowed in speech synthesizers.

## Topics

### Rendering speech
- [func synthesizeSpeechRequest(AVSpeechSynthesisProviderRequest)](./avspeechsynthesisprovideraudiounit/synthesizespeechrequest%28_%29.md)
  Sets the text to synthesize and the voice to use.
- [class AVSpeechSynthesisProviderRequest](./avspeechsynthesisproviderrequest.md)
  An object that represents the text to synthesize and the voice to use.
### Supplying metadata
- [typealias AVSpeechSynthesisProviderOutputBlock](./avspeechsynthesisprovideroutputblock.md)
  A type that represents the method for sending marker information to the host.
- [var speechSynthesisOutputMetadataBlock: AVSpeechSynthesisProviderOutputBlock?](./avspeechsynthesisprovideraudiounit/speechsynthesisoutputmetadatablock.md)
  A block that subclasses use to send marker information to the host.
### Getting and setting voices
- [var speechVoices: [AVSpeechSynthesisProviderVoice]](./avspeechsynthesisprovideraudiounit/speechvoices.md)
  A list of voices the audio unit provides to the system.
- [class AVSpeechSynthesisProviderVoice](./avspeechsynthesisprovidervoice.md)
  An object that represents a voice that an audio unit provides to its host.
### Cancelling a request
- [func cancelSpeechRequest()](./avspeechsynthesisprovideraudiounit/cancelspeechrequest%28%29.md)
  Informs the audio unit to discard the speech request.

## Relationships

### Inherits From
- [AUAudioUnit](../AudioToolbox/auaudiounit.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Speech synthesis Audio Unit
- [Creating a custom speech synthesizer](./creating-a-custom-speech-synthesizer.md)
  Use your custom voices to synthesize speech by building a speech synthesis provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovideraudiounit)*