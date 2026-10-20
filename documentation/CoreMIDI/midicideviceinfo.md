# MIDICIDeviceInfo

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

An object that provides basic information about a MIDI-CI device.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
class MIDICIDeviceInfo
```

```objc
@interface MIDICIDeviceInfo : NSObject
```

## Topics

### Creating Device Information
- [init(destination: MIDIEntityRef, manufacturer: Data, family: Data, model: Data, revision: Data)](./midicideviceinfo/init%28destination,manufacturer,family,model,revision%29.md)
  Creates a new device information instance.
### Inspecting a Device
- [var manufacturerID: Data](./midicideviceinfo/manufacturerid.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var family: Data](./midicideviceinfo/family.md)
  The family to which the device belongs.
- [var modelNumber: Data](./midicideviceinfo/modelnumber.md)
  The model number of the device.
- [var revisionLevel: Data](./midicideviceinfo/revisionlevel.md)
  The revision number of the device model number.
- [var midiDestination: MIDIEndpointRef](./midicideviceinfo/mididestination.md)
  The MIDI destination the device’s MIDI entity uses for capability inquiries.
### Initializers
- [init?(coder: NSCoder)](./midicideviceinfo/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Inspecting a Responder
- [typealias MIDICIInitiatiorMUID](./midiciinitiatiormuid.md)
  The unique MIDI-CI negotiation identifier to use for a responder connection.
- [var initiators: [MIDICIInitiatiorMUID]](./midiciresponder/initiators.md)
  An array of initiators.
- [struct MIDICIDeviceIdentification](./midicideviceidentification.md)
  A structure that describes a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](./midiciresponder/deviceinfo.md)
  The MIDI-CI device’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo)*