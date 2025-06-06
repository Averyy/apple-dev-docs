# AVSpeechSynthesizer

**Framework**: Avfaudio  
**Kind**: class

An object that produces synthesized speech from text utterances and enables monitoring or controlling of ongoing speech.

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
class AVSpeechSynthesizer
```

#### Overview

To speak some text, create an [`AVSpeechUtterance`](avspeechutterance.md) instance that contains the text and pass it to [`speak(_:)`](avspeechsynthesizer/speak(_:).md) on a speech synthesizer instance. You can optionally also retrieve an [`AVSpeechSynthesisVoice`](avspeechsynthesisvoice.md) and set it on the utterance’s [`voice`](avspeechutterance/voice.md) property to have the speech synthesizer use that voice when speaking the utterance’s text.

The speech synthesizer maintains a queue of utterances that it speaks. If the synthesizer isn’t speaking, calling [`speak(_:)`](avspeechsynthesizer/speak(_:).md) begins speaking that utterance either immediately or after pausing for its [`preUtteranceDelay`](avspeechutterance/preutterancedelay.md), if necessary. If the synthesizer is speaking, the synthesizer adds utterances to a queue and speaks them in the order it receives them.

After speech begins, you can use the synthesizer object to pause or stop speech. After pausing, you can resume the speech from its paused point or stop the speech entirely and remove all remaining utterances in the queue.

You can monitor the speech synthesizer by examining its [`isSpeaking`](avspeechsynthesizer/isspeaking.md) and [`isPaused`](avspeechsynthesizer/ispaused.md) properties, or by setting a delegate that conforms to [`AVSpeechSynthesizerDelegate`](avspeechsynthesizerdelegate.md). The delegate receives significant events as they occur during speech synthesis.

An `AVSpeechSynthesizer` also controls the route where the speech plays. For more information, see Directing speech output.

> **Note**:  The system doesn’t automatically retain the speech synthesizer, so you need to manually retain it until speech concludes.

## Topics

### Controlling speech
- [func speak(AVSpeechUtterance)](avspeechsynthesizer/speak(_:).md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func continueSpeaking() -> Bool](avspeechsynthesizer/continuespeaking.md)
  Resumes speech from its paused point.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/pausespeaking(at:).md)
  Pauses speech at the boundary you specify.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/stopspeaking(at:).md)
  Stops speech at the boundary you specify.
- [enum AVSpeechBoundary](avspeechboundary.md)
  Specifies when to pause or stop speech.
### Inspecting a speech synthesizer
- [var isSpeaking: Bool](avspeechsynthesizer/isspeaking.md)
  A Boolean value that indicates whether the speech synthesizer is speaking or is in a paused state and has utterances to speak.
- [var isPaused: Bool](avspeechsynthesizer/ispaused.md)
  A Boolean value that indicates whether a speech synthesizer is in a paused state.
### Managing the delegate
- [var delegate: (any AVSpeechSynthesizerDelegate)?](avspeechsynthesizer/delegate.md)
  The delegate object for the speech synthesizer.
- [protocol AVSpeechSynthesizerDelegate](avspeechsynthesizerdelegate.md)
  A delegate protocol that contains optional methods you can implement to respond to events that occur during speech synthesis.
### Directing speech output
- [var usesApplicationAudioSession: Bool](avspeechsynthesizer/usesapplicationaudiosession.md)
  A Boolean value that specifies whether the app manages the audio session.
- [var mixToTelephonyUplink: Bool](avspeechsynthesizer/mixtotelephonyuplink.md)
  A Boolean value that specifies whether to send synthesized speech to an active call.
- [var outputChannels: [AVAudioSessionChannelDescription]?](avspeechsynthesizer/outputchannels.md)
  An array of audio session channels to route generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback)](avspeechsynthesizer/write(_:tobuffercallback:).md)
  Generates speech for the utterance and invokes the callback with the audio buffer.
- [AVSpeechSynthesizer.BufferCallback](avspeechsynthesizer/buffercallback.md)
  A type that defines a callback that receives a buffer of generated speech.
- [func write(AVSpeechUtterance, toBufferCallback: AVSpeechSynthesizer.BufferCallback, toMarkerCallback: AVSpeechSynthesizer.MarkerCallback)](avspeechsynthesizer/write(_:tobuffercallback:tomarkercallback:).md)
  Generates audio buffers and associated metadata for storage or further speech synthesis processing.
- [AVSpeechSynthesizer.MarkerCallback](avspeechsynthesizer/markercallback.md)
  A type that defines a callback that receives speech markers.
### Enabling personal voices
- [class var personalVoiceAuthorizationStatus: AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.type.property.md)
  Your app’s authorization to use personal voices.
- [class let availableVoicesDidChangeNotification: NSNotification.Name](avspeechsynthesizer/availablevoicesdidchangenotification.md)
  A notification that indicates a change in available voices for speech synthesis.
- [class func requestPersonalVoiceAuthorization(completionHandler: (AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus) -> Void)](avspeechsynthesizer/requestpersonalvoiceauthorization(completionhandler:).md)
  Prompts the user to authorize your app to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum.md)
  An enumeration that models the personal voices authorization status.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFAudio/avspeechsynthesizer)*