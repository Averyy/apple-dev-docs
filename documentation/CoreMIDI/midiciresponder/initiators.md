# initiators

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

An array of initiators.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var initiators: [MIDICIInitiatiorMUID] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * initiators;
```

## See Also

### Inspecting a Responder
- [typealias MIDICIInitiatiorMUID](../midiciinitiatiormuid.md)
  The unique MIDI-CI negotiation identifier to use for a responder connection.
- [struct MIDICIDeviceIdentification](../midicideviceidentification.md)
  A structure that describes a MIDI-CI device.
- [class MIDICIDeviceInfo](../midicideviceinfo.md)
  An object that provides basic information about a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](./deviceinfo.md)
  The MIDI-CI device’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/initiators)*