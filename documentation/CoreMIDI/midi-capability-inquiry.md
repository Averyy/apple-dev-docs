# MIDI Capability Inquiry

**Framework**: Core MIDI

Provide support for bidirectional discovery and configuration of devices.

#### Overview

MIDI Capability Inquiry (MIDI-CI) uses bidirectional communication to enable devices to exchange information about their capabilities and automatically configure themselves to work together. MIDI-CI discovers and configures devices using the following means:

- Profile configuration. Profiles define a standard set of rules for how devices respond to MIDI messages. For example, devices that support a piano profile respond to messages common to a piano, such as note on and off, velocity, and pedaling.
- Property exchange. Devices can use a set of System Exclusive (SysEx) messages to find and control various properties of other devices.
- Protocol negotiation. MIDI 2.0 devices can select between using the MIDI 1.0 or 2.0 protocols, falling back to 1.0 when not supported by other devices.

MIDI-CI defines two roles in the communication between devices:  and . Client processes acting as the initiator use the [`MIDICISession`](midicisession.md) API, which allows for profile and property configuration of the associated responder. Client processes that advertise their own profile and property capabilities use the [`MIDICIResponder`](midiciresponder.md) API, which sends responder-originated messages to initiators.

## Topics

### Capability Inquiry
- [class MIDICIDiscoveryManager](midicidiscoverymanager.md)
  A singleton object that performs systemwide MIDI-CI discovery.
- [class MIDICISession](midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [class MIDICIResponder](midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-capability-inquiry)*