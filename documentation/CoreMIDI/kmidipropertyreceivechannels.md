# kMIDIPropertyReceiveChannels

**Framework**: Core MIDI  
**Kind**: var

The bitmap of channels on which the object receives messages.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyReceiveChannels: CFString
```

#### Discussion

You can use this property in the following scenarios:

- Drivers can set this property on their entities and endpoints.
- Studio setup editors can allow the user to set this property on external endpoints.
- Virtual destinations can set this property on their endpoints.

## See Also

- [let kMIDIPropertyTransmitChannels: CFString](kmidipropertytransmitchannels.md)
  The bitmap of channels on which the object transmits messages.
- [let kMIDIPropertyMaxReceiveChannels: CFString](kmidipropertymaxreceivechannels.md)
  The maximum number of MIDI channels on which a device may simultaneously receive channel messages.
- [let kMIDIPropertyMaxTransmitChannels: CFString](kmidipropertymaxtransmitchannels.md)
  The maximum number of MIDI channels on which a device may simultaneously transmit channel messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyreceivechannels)*