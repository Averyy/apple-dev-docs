# IOUserAudioStreamTerminalType

**Framework**: AudioDriverKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the terminal type of an audio stream.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
enum IOUserAudioStreamTerminalType : uint32_t;
```

## Topics

### Speakers
- [Speaker](./iouseraudiostreamterminaltype/speaker.md)
  An audio speaker.
- [ReceiverSpeaker](./iouseraudiostreamterminaltype/receiverspeaker.md)
  A speaker on a telephone handset receiver.
- [LFESpeaker](./iouseraudiostreamterminaltype/lfespeaker.md)
  A speaker for low-frequency effects.
### Microphones
- [Microphone](./iouseraudiostreamterminaltype/microphone.md)
  An audio microphone.
- [HeadsetMicrophone](./iouseraudiostreamterminaltype/headsetmicrophone.md)
  A microphone attached to a headset.
- [ReceiverMicrophone](./iouseraudiostreamterminaltype/receivermicrophone.md)
  A microphone on a telephone receiver.
### Headphones and Headsets
- [Headphones](./iouseraudiostreamterminaltype/headphones.md)
  An audio headphones device.
### Accessibility Devices
- [TTY](./iouseraudiostreamterminaltype/tty.md)
  A device that serves as a teletypewriter (TTY) terminal.
### Audio Interfaces
- [Line](./iouseraudiostreamterminaltype/line.md)
  A line-level stream.
- [DigitalAudioInterface](./iouseraudiostreamterminaltype/digitalaudiointerface.md)
  A stream to or from a digital audio interface, defined by ISO 60958.
### Enumeration Cases
- [DisplayPort](./iouseraudiostreamterminaltype/displayport.md)
- [HDMI](./iouseraudiostreamterminaltype/hdmi.md)
- [Unknown](./iouseraudiostreamterminaltype/unknown.md)

## See Also

### Working with Stream Terminals
- [SetTerminalType](../iouseraudiostream/setterminaltype.md)
  Sets the terminal type of the stream.
- [GetTerminalType](../iouseraudiostream/getterminaltype.md)
  Gets the terminal type of the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiostreamterminaltype)*