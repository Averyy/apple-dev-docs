# MIDICIInitiatiorMUID

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

The unique MIDI-CI negotiation identifier to use for a responder connection.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias MIDICIInitiatiorMUID = NSNumber
```

```c
typedef NSNumber * MIDICIInitiatiorMUID;
```

## Discussion

As required by the MIDI-CI specification, this value is a randomly assigned 28-bit integer.

## See Also

### Inspecting a Responder
- [var initiators: [MIDICIInitiatiorMUID]](./midiciresponder/initiators.md)
  An array of initiators.
- [struct MIDICIDeviceIdentification](./midicideviceidentification.md)
  A structure that describes a MIDI-CI device.
- [class MIDICIDeviceInfo](./midicideviceinfo.md)
  An object that provides basic information about a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](./midiciresponder/deviceinfo.md)
  The MIDI-CI device’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciinitiatiormuid)*