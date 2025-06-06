# kMIDIPropertyProtocolID

**Framework**: Core MIDI  
**Kind**: var

The native protocol in which the endpoint communicates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let kMIDIPropertyProtocolID: CFString
```

#### Discussion

The system sets this value on endpoints when it creates them. Drivers can dynamically change the endpoint’s protocol as a result of a MIDI-CI negotiation, by setting this property.

Clients can observe changes to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/kmidipropertyprotocolid)*