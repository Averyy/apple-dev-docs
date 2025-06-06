# MIDICIDeviceIdentification

**Framework**: Core MIDI  
**Kind**: struct

A structure that describes a MIDI-CI device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MIDICIDeviceIdentification
```

## Topics

### Configuring Device Identification
- [var manufacturer: (UInt8, UInt8, UInt8)](midicideviceidentification/manufacturer.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var modelNumber: (UInt8, UInt8)](midicideviceidentification/modelnumber.md)
  The device model number.
- [var family: (UInt8, UInt8)](midicideviceidentification/family.md)
  The group of familes to which the device belongs.
- [var revisionLevel: (UInt8, UInt8, UInt8, UInt8)](midicideviceidentification/revisionlevel.md)
  The revision number of the device model number.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8)](midicideviceidentification/reserved.md)
  A reserved field whose value is always zero.
### Initializers
- [init()](midicideviceidentification/init.md)
- [init(manufacturer: (UInt8, UInt8, UInt8), family: (UInt8, UInt8), modelNumber: (UInt8, UInt8), revisionLevel: (UInt8, UInt8, UInt8, UInt8), reserved: (UInt8, UInt8, UInt8, UInt8, UInt8))](midicideviceidentification/init(manufacturer:family:modelnumber:revisionlevel:reserved:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias MIDICIInitiatiorMUID](midiciinitiatiormuid.md)
  The unique MIDI-CI negotiation identifier to use for a responder connection.
- [var initiators: [MIDICIInitiatiorMUID]](midiciresponder/initiators.md)
  An array of initiators.
- [class MIDICIDeviceInfo](midicideviceinfo.md)
  An object that provides basic information about a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](midiciresponder/deviceinfo.md)
  The MIDI-CI device’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceidentification)*