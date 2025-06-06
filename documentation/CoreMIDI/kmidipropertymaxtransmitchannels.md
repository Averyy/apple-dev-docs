# kMIDIPropertyMaxTransmitChannels

**Framework**: Core MIDI  
**Kind**: var

The maximum number of MIDI channels on which a device may simultaneously transmit channel messages.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyMaxTransmitChannels: CFString
```

#### Discussion

Common values are 0, 1, and 16.

## See Also

- [let kMIDIPropertyReceiveChannels: CFString](kmidipropertyreceivechannels.md)
  The bitmap of channels on which the object receives messages.
- [let kMIDIPropertyTransmitChannels: CFString](kmidipropertytransmitchannels.md)
  The bitmap of channels on which the object transmits messages.
- [let kMIDIPropertyMaxReceiveChannels: CFString](kmidipropertymaxreceivechannels.md)
  The maximum number of MIDI channels on which a device may simultaneously receive channel messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertymaxtransmitchannels)*