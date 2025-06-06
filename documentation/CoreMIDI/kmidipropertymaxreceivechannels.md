# kMIDIPropertyMaxReceiveChannels

**Framework**: Core MIDI  
**Kind**: var

The maximum number of MIDI channels on which a device may simultaneously receive channel messages.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyMaxReceiveChannels: CFString
```

#### Discussion

The property value ranges from 0 to 16. Values for this property indicate:

- 0 for devices that only respond to system messages
- 1 for nonmultitimbral devices
- 2 to 15 for multitimbral devices with fewer than 16 voices
- 16 for fully multitimbral devices

## See Also

- [let kMIDIPropertyReceiveChannels: CFString](kmidipropertyreceivechannels.md)
  The bitmap of channels on which the object receives messages.
- [let kMIDIPropertyTransmitChannels: CFString](kmidipropertytransmitchannels.md)
  The bitmap of channels on which the object transmits messages.
- [let kMIDIPropertyMaxTransmitChannels: CFString](kmidipropertymaxtransmitchannels.md)
  The maximum number of MIDI channels on which a device may simultaneously transmit channel messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertymaxreceivechannels)*