# AVAudioInputNode

**Framework**: AVFAudio  
**Kind**: class

An object that connects to the system’s audio input.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class AVAudioInputNode
```

#### Overview

This node connects to the system’s audio input when rendering to or from an audio device. In manual rendering mode, this node supplies input data to the engine.

This audio node has one element. The format of the input scope reflects:

- The audio hardware sample rate and channel count when it connects to hardware.
- The format of the PCM audio data that the node supplies to the engine in manual rendering mode. For more information, see [`setManualRenderingInputPCMFormat(_:inputBlock:)`](avaudioinputnode/setmanualrenderinginputpcmformat(_:inputblock:).md)

When rendering from an audio device, the input node doesn’t support format conversion. In this case, the format of the output scope must be the same as the input and the formats for all nodes connected to the input chain.

In manual rendering mode, the format of the output scope is initially the same as the input, but you may set it to a different format, which converts the node.

> ❗ **Important**:  This class has no methods of its own. It implements the methods that the [`AVAudioMixing`](avaudiomixing.md) protocol defines, as well as those of the [`AVAudio3DMixing`](avaudio3dmixing.md) protocol, which the [`AVAudioMixing`](avaudiomixing.md) protocol adopts. For more information, see [`AVAudioMixing`](avaudiomixing.md) and [`AVAudio3DMixing`](avaudio3dmixing.md).

 This class has no methods of its own. It implements the methods that the [`AVAudioMixing`](avaudiomixing.md) protocol defines, as well as those of the [`AVAudio3DMixing`](avaudio3dmixing.md) protocol, which the [`AVAudioMixing`](avaudiomixing.md) protocol adopts. For more information, see [`AVAudioMixing`](avaudiomixing.md) and [`AVAudio3DMixing`](avaudio3dmixing.md).

## Topics

### Manually Giving Data to an Audio Engine
- [func setManualRenderingInputPCMFormat(AVAudioFormat, inputBlock: AVAudioIONodeInputBlock) -> Bool](avaudioinputnode/setmanualrenderinginputpcmformat(_:inputblock:).md)
  Supplies the data through the input node to the engine while operating in the manual rendering mode.
- [typealias AVAudioIONodeInputBlock](avaudioionodeinputblock.md)
  The type that represents a block to render operation calls to get input data when in manual rendering mode.
### Getting and Setting Voice Processing Properties
- [var isVoiceProcessingInputMuted: Bool](avaudioinputnode/isvoiceprocessinginputmuted.md)
  A Boolean that indicates whether the input of the voice processing unit is in a muted state.
- [var isVoiceProcessingBypassed: Bool](avaudioinputnode/isvoiceprocessingbypassed.md)
  A Boolean that indicates whether the node bypasses all microphone uplink processing of the voice-processing unit.
- [var isVoiceProcessingAGCEnabled: Bool](avaudioinputnode/isvoiceprocessingagcenabled.md)
  A Boolean that indicates whether automatic gain control on the processed microphone uplink signal is active.
- [var voiceProcessingOtherAudioDuckingConfiguration: AVAudioVoiceProcessingOtherAudioDuckingConfiguration](avaudioinputnode/voiceprocessingotheraudioduckingconfiguration.md)
  The ducking configuration of nonvoice audio.
- [struct AVAudioVoiceProcessingOtherAudioDuckingConfiguration](avaudiovoiceprocessingotheraudioduckingconfiguration.md)
  The configuration of ducking non-voice audio.
### Handling Muted Speech Events
- [func setMutedSpeechActivityEventListener(((AVAudioVoiceProcessingSpeechActivityEvent) -> Void)?) -> Bool](avaudioinputnode/setmutedspeechactivityeventlistener(_:).md)
- [enum AVAudioVoiceProcessingSpeechActivityEvent](avaudiovoiceprocessingspeechactivityevent.md)
  Types of speech activity events.

## Relationships

### Inherits From
- [AVAudioIONode](avaudioionode.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioNode](avaudionode.md)
  An object you use for audio generation, processing, or an I/O block.
- [class AVAudioOutputNode](avaudiooutputnode.md)
  An object that connects to the system’s audio output.
- [class AVAudioIONode](avaudioionode.md)
  An object that performs audio input or output in the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioinputnode)*