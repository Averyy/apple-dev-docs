# MIDI Thru Connection

**Framework**: Core MIDI

Create play-through connections between sources and destinations.

#### Overview

Use play-through connections, instead of performing MIDI Thru operations, to reduce the overhead of moving MIDI messages between the server and the client. This API provides a simple interface to perform a variety of transformations.

## Topics

### Finding Connections
- [func MIDIThruConnectionFind(CFString, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](midithruconnectionfind(_:_:).md)
  Finds the persistent thru connections for the specified client.
### Managing Connections
- [func MIDIThruConnectionCreate(CFString?, CFData, UnsafeMutablePointer<MIDIThruConnectionRef>) -> OSStatus](midithruconnectioncreate(_:_:_:).md)
  Creates a MIDI thru connection.
- [func MIDIThruConnectionDispose(MIDIThruConnectionRef) -> OSStatus](midithruconnectiondispose(_:).md)
  Disposes a MIDI thru connection.
- [typealias MIDIThruConnectionRef](midithruconnectionref.md)
  An opaque reference to a play-through connection.
- [struct MIDIThruConnectionEndpoint](midithruconnectionendpoint.md)
  A source or destination in a MIDI thru connection.
- [Endpoint Configuration](endpoint-configuration.md)
  Values that define the supported endpoint configurations.
### Configuring Parameters
- [struct MIDIThruConnectionParams](midithruconnectionparams.md)
  A set of MIDI routings and transformations.
- [func MIDIThruConnectionParamsSize(UnsafePointer<MIDIThruConnectionParams>) -> Int](midithruconnectionparamssize(_:).md)
  Returns the size of a MIDI thru connection parameters object.
- [func MIDIThruConnectionParamsInitialize(UnsafeMutablePointer<MIDIThruConnectionParams>)](midithruconnectionparamsinitialize(_:).md)
  Initializes a parameters object with its default values.
- [func MIDIThruConnectionGetParams(MIDIThruConnectionRef, UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](midithruconnectiongetparams(_:_:).md)
  Returns the thru connection’s parameters.
- [func MIDIThruConnectionSetParams(MIDIThruConnectionRef, CFData) -> OSStatus](midithruconnectionsetparams(_:_:).md)
  Updates a thru connection’s parameters.
### Transforming Values
- [struct MIDIValueMap](midivaluemap.md)
  A custom lookup table to transform MIDI 7-bit values, as contained in note numbers, velocities, control values, and so on.
- [struct MIDIControlTransform](midicontroltransform.md)
  A structure that describes the transformation of MIDI control change events.
- [struct MIDITransform](miditransform.md)
  The transformation of a single type of MIDI event.
- [enum MIDITransformType](miditransformtype.md)
  Values that specify the type of MIDI transformation.
- [enum MIDITransformControlType](miditransformcontroltype.md)
  A set of values that indicate how to interpret control numbers.

## See Also

- [MIDI Services](midi-services.md)
  Communicate with hardware using Universal MIDI Packets.
- [MIDI System Setup](midi-system-setup.md)
  Configure the global MIDI system.
- [MIDI Bluetooth](midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](midi-messages.md)
  Create and configure messages.
- [MIDI Networking](midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-thru-connection)*