# MIDICIDeviceInfo

**Framework**: Core MIDI  
**Kind**: class

An object that provides basic information about a MIDI-CI device.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
class MIDICIDeviceInfo
```

## Topics

### Creating Device Information
- [init(destination: MIDIEntityRef, manufacturer: Data, family: Data, model: Data, revision: Data)](midicideviceinfo/init(destination:manufacturer:family:model:revision:).md)
  Creates a new device information instance.
### Inspecting a Device
- [var manufacturerID: Data](midicideviceinfo/manufacturerid.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var family: Data](midicideviceinfo/family.md)
  The family to which the device belongs.
- [var modelNumber: Data](midicideviceinfo/modelnumber.md)
  The model number of the device.
- [var revisionLevel: Data](midicideviceinfo/revisionlevel.md)
  The revision number of the device model number.
- [var midiDestination: MIDIEndpointRef](midicideviceinfo/mididestination.md)
  The MIDI destination the device’s MIDI entity uses for capability inquiries.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [typealias MIDICIInitiatiorMUID](midiciinitiatiormuid.md)
  The unique MIDI-CI negotiation identifier to use for a responder connection.
- [var initiators: [MIDICIInitiatiorMUID]](midiciresponder/initiators.md)
  An array of initiators.
- [struct MIDICIDeviceIdentification](midicideviceidentification.md)
  A structure that describes a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](midiciresponder/deviceinfo.md)
  The MIDI-CI device’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo)*