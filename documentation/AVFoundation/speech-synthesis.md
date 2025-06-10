# Speech synthesis

**Framework**: AVFoundation

Configure voices to speak strings of text.

#### Overview

The Speech Synthesis framework manages voice and speech synthesis, and requires two primary tasks:

Create an [`AVSpeechUtterance`](https://developer.apple.com/documentation/AVFAudio/AVSpeechUtterance) instance that contains the text to speak. Optionally, configure speech parameters, such as voice and rate, for each utterance.

```swift
// Create an utterance.
let utterance = AVSpeechUtterance(string: "The quick brown fox jumped over the lazy dog.")

// Configure the utterance.
utterance.rate = 0.57
utterance.pitchMultiplier = 0.8
utterance.postUtteranceDelay = 0.2
utterance.volume = 0.8

// Retrieve the British English voice.
let voice = AVSpeechSynthesisVoice(language: "en-GB")

// Assign the voice to the utterance.
utterance.voice = voice
```

Pass the utterance to an [`AVSpeechSynthesizer`](https://developer.apple.com/documentation/AVFAudio/AVSpeechSynthesizer) instance to produce spoken audio.

```swift
// Create a speech synthesizer.
let synthesizer = AVSpeechSynthesizer()

// Tell the synthesizer to speak the utterance.
synthesizer.speak(utterance)
```

Optionally, use the speech synthesizer instance to control or respond to ongoing speech; for example, assign its [`delegate`](https://developer.apple.com/documentation/AVFAudio/AVSpeechSynthesizer/delegate) to receive speech event notifications.

> **Note**:  Speech generation occurs on device and isn’t sent to a server for processing.

## Topics

### Spoken text attributes
- [class AVSpeechUtterance](../AVFAudio/AVSpeechUtterance.md)
  An object that encapsulates the text for speech synthesis and parameters that affect the speech.
- [class AVSpeechSynthesisVoice](../AVFAudio/AVSpeechSynthesisVoice.md)
  A distinct voice for use in speech synthesis.
### Speech synthesis controls
- [class AVSpeechSynthesizer](../AVFAudio/AVSpeechSynthesizer.md)
  An object that produces synthesized speech from text utterances and enables monitoring or controlling of ongoing speech.
### Speech synthesis audio unit
- [class AVSpeechSynthesisProviderAudioUnit](../AVFAudio/AVSpeechSynthesisProviderAudioUnit.md)
  An object that generates speech from text.

## See Also

- [Audio playback, recording, and processing](audio-playback-recording-and-processing.md)
  Play, record, and process audio; configure your app’s system audio behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/speech-synthesis)*