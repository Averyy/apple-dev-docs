# Core MIDI

**Framework**: Core MIDI  
**Kind**: module

Communicate with MIDI devices such as hardware keyboards and synthesizers.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

#### Overview

The Core MIDI framework provides APIs to communicate with MIDI (Musical Instrument Digital Interface) devices, including hardware keyboards and synthesizers. Connect from an iOS device using the dock connector or a network. For more information about using the dock connector, see the [`MFi Program`](https://developer.apple.comhttps://developer.apple.com/programs/mfi/).

## Topics

### Services
- [MIDI Services](midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI System Setup](midi-system-setup.md)
  Configure the global MIDI system.
- [MIDI Bluetooth](midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](midi-messages.md)
  Create and configure messages.
- [MIDI Thru Connection](midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.
### Reference
- [Core MIDI Structures](core-midi-structures.md)
- [Core MIDI Enumerations](core-midi-enumerations.md)
- [Core MIDI Constants](core-midi-constants.md)
- [Core MIDI Functions](core-midi-functions.md)
- [Core MIDI Data Types](core-midi-data-types.md)
- [Core MIDI Macros](coremidi-macros.md)
### Articles
- [kMIDIObjectType_ExternalMask](kmidiobjecttype_externalmask.md)
  A bit mask indicating that a device is external.
- [Deprecated Symbols](midi_system_setup-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Classes
- [class MIDI2DeviceInfo](midi2deviceinfo.md)
- [class MIDICIDevice](midicidevice.md)
- [class MIDICIDeviceManager](midicidevicemanager.md)
- [class MIDICIDiscoveredNode](midicidiscoverednode.md)
  A discovered MIDI-CI node that represents a MIDI source and destination that respond to capability inquiries.
- [class MIDIUMPCIProfile](midiumpciprofile.md)
- [class MIDIUMPEndpoint](midiumpendpoint.md)
- [class MIDIUMPEndpointManager](midiumpendpointmanager.md)
- [class MIDIUMPFunctionBlock](midiumpfunctionblock.md)
- [class MIDIUMPMutableEndpoint](midiumpmutableendpoint.md)
- [class MIDIUMPMutableFunctionBlock](midiumpmutablefunctionblock.md)
### Variables
- [var kMIDINoteAttributeManufacturerSpecific: Int](kmidinoteattributemanufacturerspecific.md)
- [var kMIDINoteAttributeNone: Int](kmidinoteattributenone.md)
- [var kMIDINoteAttributePitch: Int](kmidinoteattributepitch.md)
- [var kMIDINoteAttributeProfileSpecific: Int](kmidinoteattributeprofilespecific.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreMIDI)*