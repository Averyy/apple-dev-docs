# AVSpeechUtterance

**Framework**: AVFAudio  
**Kind**: class

An object that encapsulates the text for speech synthesis and parameters that affect the speech.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVSpeechUtterance
```

#### Overview

An `AVSpeechUtterance` is the basic unit of speech synthesis.

To synthesize speech, create an `AVSpeechUtterance` instance with text you want a speech synthesizer to speak. Optionally, change the [`voice`](avspeechutterance/voice.md), [`pitchMultiplier`](avspeechutterance/pitchmultiplier.md), [`volume`](avspeechutterance/volume.md), [`rate`](avspeechutterance/rate.md), [`preUtteranceDelay`](avspeechutterance/preutterancedelay.md), or [`postUtteranceDelay`](avspeechutterance/postutterancedelay.md) parameters for the utterance. Pass the utterance to an instance of [`AVSpeechSynthesizer`](avspeechsynthesizer.md) to begin speech, or enqueue the utterance to speak later if the synthesizer is already speaking.

Split a body of text into multiple utterances if you want to apply different speech parameters. For example, you can emphasize a sentence by increasing the pitch and decreasing the rate of that utterance relative to others, or you can introduce pauses between sentences by putting each into an utterance with a leading or trailing delay.

Set and use the [`AVSpeechSynthesizerDelegate`](avspeechsynthesizerdelegate.md) to receive notifications when the synthesizer starts or finishes speaking an utterance. Create an utterance for each meaningful unit in a body of text if you want to receive notifications as its speech progresses.

## Topics

### Creating an utterance
- [init(string: String)](avspeechutterance/init(string:).md)
  Creates an utterance with the text string that you specify for the speech synthesizer to speak.
- [init(attributedString: NSAttributedString)](avspeechutterance/init(attributedstring:).md)
  Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.
- [let AVSpeechSynthesisIPANotationAttribute: String](avspeechsynthesisipanotationattribute.md)
  A string that contains International Phonetic Alphabet (IPA) symbols the speech synthesizer uses to control pronunciation of certain words or phrases.
- [init?(ssmlRepresentation: String)](avspeechutterance/init(ssmlrepresentation:).md)
  Creates a speech utterance with an Speech Synthesis Markup Language (SSML) string.
### Configuring an utterance
- [var voice: AVSpeechSynthesisVoice?](avspeechutterance/voice.md)
  The voice the speech synthesizer uses when speaking the utterance.
- [var pitchMultiplier: Float](avspeechutterance/pitchmultiplier.md)
  The baseline pitch the speech synthesizer uses when speaking the utterance.
- [var volume: Float](avspeechutterance/volume.md)
  The volume the speech synthesizer uses when speaking the utterance.
- [var prefersAssistiveTechnologySettings: Bool](avspeechutterance/prefersassistivetechnologysettings.md)
  A Boolean that specifies whether assistive technology settings take precedence over the property values of this utterance.
### Configuring utterance timing
- [var rate: Float](avspeechutterance/rate.md)
  The rate the speech synthesizer uses when speaking the utterance.
- [let AVSpeechUtteranceMinimumSpeechRate: Float](avspeechutteranceminimumspeechrate.md)
  The minimum rate the speech synthesizer uses when speaking an utterance.
- [let AVSpeechUtteranceMaximumSpeechRate: Float](avspeechutterancemaximumspeechrate.md)
  The maximum rate the speech synthesizer uses when speaking an utterance.
- [let AVSpeechUtteranceDefaultSpeechRate: Float](avspeechutterancedefaultspeechrate.md)
  The default rate the speech synthesizer uses when speaking an utterance.
- [var preUtteranceDelay: TimeInterval](avspeechutterance/preutterancedelay.md)
  The amount of time the speech synthesizer pauses before speaking the utterance.
- [var postUtteranceDelay: TimeInterval](avspeechutterance/postutterancedelay.md)
  The amount of time the speech synthesizer pauses after speaking an utterance before handling the next utterance in the queue.
### Inspecting utterance text
- [var speechString: String](avspeechutterance/speechstring.md)
  A string that contains the text for speech synthesis.
- [var attributedSpeechString: NSAttributedString](avspeechutterance/attributedspeechstring.md)
  An attributed string that contains the text for speech synthesis.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class AVSpeechSynthesisVoice](avspeechsynthesisvoice.md)
  A distinct voice for use in speech synthesis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance)*