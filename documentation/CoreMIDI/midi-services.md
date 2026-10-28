# MIDI Services

**Framework**: Core MIDI  
**Role**: API Collection

Communicate with hardware using Universal MIDI Packets.

## Overview

MIDI drivers own and control physical MIDI devices, which include hardware such as USB interfaces, MIDI keyboards, and so on. A MIDI device may have multiple logically distinct subcomponents. For example, one device may contain a MIDI synthesizer and a pair of MIDI ports, both addressable over a USB port. Each element of a device is a MIDI entity.

A MIDI entity can have any number of MIDI endpoints, each of which is a source or destination of a 16-channel MIDI stream. Grouping a device’s endpoints into entities provides the system enough information for an app to make reasonable default assumptions about how to communicate bidirectionally with each entity, as is necessary in MIDI librarian apps.

Core MIDI attaches a collection of properties to each object it manages. Object properties can be:

- Dynamic characteristics of a device, such as MIDI receive channel and system-exclusive (SysEx) IDs.
- Determined by user preference; for example, choice of icon, and whether or not the device appears in lists of possible controllers.
- Static properties that you can’t look up in a database using the device’s manufacturer and model name.

The Core MIDI framework uses interprocess communication (IPC) to communicate with a server process, the MIDI server. The server process in turn loads the MIDI driver and manages all communication with it.

## Topics

### MIDI object configuration
- [func MIDIObjectFindByUniqueID(MIDIUniqueID, UnsafeMutablePointer<MIDIObjectRef>?, UnsafeMutablePointer<MIDIObjectType>?) -> OSStatus](./midiobjectfindbyuniqueid%28_,_,_%29.md)
  Locates a device, entity, or endpoint by its unique identifier.
- [typealias MIDIObjectRef](./midiobjectref.md)
  The common base class for many of the framework’s objects.
- [MIDI Object Properties](./midi-object-properties.md)
  Configure the properties of MIDI objects.
### Client management
- [Incorporating MIDI 2 into your apps](./incorporating-midi-2-into-your-apps.md)
  Add precision and improve musical control for your MIDI apps.
- [func MIDIClientCreate(CFString, MIDINotifyProc?, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](./midiclientcreate%28_,_,_,_%29.md)
  Creates a MIDI client.
- [func MIDIClientCreateWithBlock(CFString, UnsafeMutablePointer<MIDIClientRef>, MIDINotifyBlock?) -> OSStatus](./midiclientcreatewithblock%28_,_,_%29.md)
  Creates a MIDI client with a callback block.
- [func MIDIClientDispose(MIDIClientRef) -> OSStatus](./midiclientdispose%28_%29.md)
  Disposes of a MIDI client.
- [typealias MIDIClientRef](./midiclientref.md)
  An object that maintains per-client state.
### Device lookup
- [func MIDIGetNumberOfDevices() -> Int](./midigetnumberofdevices%28%29.md)
  Returns the number of devices in the system.
- [func MIDIGetDevice(Int) -> MIDIDeviceRef](./midigetdevice%28_%29.md)
  Returns a device from the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](./midigetnumberofexternaldevices%28%29.md)
  Returns the number of external MIDI devices in the system.
- [func MIDIGetExternalDevice(Int) -> MIDIDeviceRef](./midigetexternaldevice%28_%29.md)
  Returns one of the external devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](./mididevicegetnumberofentities%28_%29.md)
  Returns the number of entities in a device.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](./mididevicegetentity%28_,_%29.md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](./midideviceref.md)
  A MIDI device that contains entities.
### Entity lookup
- [func MIDIEntityGetDevice(MIDIEntityRef, UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](./midientitygetdevice%28_,_%29.md)
  Returns an entity’s device.
- [func MIDIEntityGetNumberOfSources(MIDIEntityRef) -> Int](./midientitygetnumberofsources%28_%29.md)
  Returns the number of sources in an entity.
- [func MIDIEntityGetSource(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetsource%28_,_%29.md)
  Returns one of an entity’s sources.
- [func MIDIEntityGetNumberOfDestinations(MIDIEntityRef) -> Int](./midientitygetnumberofdestinations%28_%29.md)
  Returns the number of destinations in an entity.
- [func MIDIEntityGetDestination(MIDIEntityRef, Int) -> MIDIEndpointRef](./midientitygetdestination%28_,_%29.md)
  Returns one of an entity’s destinations.
- [typealias MIDIEntityRef](./midientityref.md)
  An entity that a device owns and that contains endpoints.
### Port management
- [func MIDIInputPortCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIPortRef>, MIDIReceiveBlock) -> OSStatus](./midiinputportcreatewithprotocol%28_,_,_,_,_%29.md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIOutputPortCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](./midioutputportcreate%28_,_,_%29.md)
  Creates an output port through which a client sends outgoing MIDI messages to any MIDI destination.
- [func MIDIPortDispose(MIDIPortRef) -> OSStatus](./midiportdispose%28_%29.md)
  Disposes of a MIDI port.
- [func MIDIPortConnectSource(MIDIPortRef, MIDIEndpointRef, UnsafeMutableRawPointer?) -> OSStatus](./midiportconnectsource%28_,_,_%29.md)
  Makes a connection from a source to a client input port.
- [func MIDIPortDisconnectSource(MIDIPortRef, MIDIEndpointRef) -> OSStatus](./midiportdisconnectsource%28_,_%29.md)
  Closes a previously established source-to-input port connection.
- [typealias MIDIPortRef](./midiportref.md)
  A MIDI connection that a client maintains.
- [typealias MIDIReceiveBlock](./midireceiveblock.md)
  A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.
### Endpoint management
- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](./midiendpointdispose%28_%29.md)
  Disposes of a virtual source or destination.
- [func MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](./midiendpointgetentity%28_,_%29.md)
  Returns an endpoint’s entity.
- [func MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutableRawPointer>?, UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OSStatus](./midiendpointgetrefcons%28_,_,_%29.md)
  Returns contextual data assigned to an endpoint.
- [func MIDIEndpointSetRefCons(MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus](./midiendpointsetrefcons%28_,_,_%29.md)
  Sets contextual data on an endpoint.
- [func MIDISourceCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](./midisourcecreatewithprotocol%28_,_,_,_%29.md)
  Creates a virtual source in a client.
- [func MIDIGetSource(Int) -> MIDIEndpointRef](./midigetsource%28_%29.md)
  Returns a source in the system.
- [func MIDIGetNumberOfSources() -> Int](./midigetnumberofsources%28%29.md)
  Returns the number of sources in the system.
- [func MIDIDestinationCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIEndpointRef>, MIDIReceiveBlock) -> OSStatus](./mididestinationcreatewithprotocol%28_,_,_,_,_%29.md)
  Creates a virtual destination in a client.
- [func MIDIGetDestination(Int) -> MIDIEndpointRef](./midigetdestination%28_%29.md)
  Returns a destination in the system.
- [func MIDIGetNumberOfDestinations() -> Int](./midigetnumberofdestinations%28%29.md)
  Returns the number of destinations in the system.
- [typealias MIDIEndpointRef](./midiendpointref.md)
  A MIDI source or destination an entity owns.
### Event list management
- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](./midieventlistinit%28_,_%29.md)
  Initializes an event list.
- [func MIDIEventListAdd(UnsafeMutablePointer<MIDIEventList>, Int, UnsafeMutablePointer<MIDIEventPacket>, MIDITimeStamp, Int, UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>](./midieventlistadd%28_,_,_,_,_,_%29.md)
  Adds an event to an event list.
- [func MIDIEventPacketNext(UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>](./midieventpacketnext%28_%29.md)
  Advances a packet pointer to the next packet in memory, if the packet is part of an event list.
- [func MIDISendEventList(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](./midisendeventlist%28_,_,_%29.md)
  Sends MIDI events to a destination.
- [func MIDIReceivedEventList(MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](./midireceivedeventlist%28_,_%29.md)
  Distributes incoming MIDI events from a source to its connected client input ports.
- [struct MIDIEventList](./midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](./midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](./unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](./unsafemutablemidieventpacketpointer.md)
### Packet list management
- [func MIDIPacketNext(UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](./midipacketnext%28_%29.md)
  Advances a MIDI packet pointer to the next packet in a package list.
- [struct MIDIPacket](./midipacket.md)
  A collection of simultaneous MIDI events.
- [struct MIDIPacketList](./midipacketlist.md)
  A list of MIDI events the system sends to or receives from an endpoint.
- [typealias MIDITimeStamp](./miditimestamp.md)
  The time on the host clock when the event occurred.
- [struct UnsafeMutableMIDIPacketListPointer](./unsafemutablemidipacketlistpointer.md)
- [struct UnsafeMutableMIDIPacketPointer](./unsafemutablemidipacketpointer.md)
### I/O management
- [struct MIDISysexSendRequest](./midisysexsendrequest.md)
  A request to asynchronously send a single system-exclusive (SysEx) event to a destination.
- [struct MIDISysexSendRequestUMP](./midisysexsendrequestump.md)
  A request to asynchronously send a single universal MIDI packet (UMP) system-exclusive (SysEx) event to a destination.
- [func MIDIFlushOutput(MIDIEndpointRef) -> OSStatus](./midiflushoutput%28_%29.md)
  Cancels all pending events that were previously scheduled to send.
- [func MIDIRestart() -> OSStatus](./midirestart%28%29.md)
  Stops and restarts MIDI I/O.
- [struct MIDIIOErrorNotification](./midiioerrornotification.md)
  A general I/O error notification.
### Errors
- [MIDI Services Errors](./midi-services-errors.md)
  Error codes for Core MIDI operations XX.
### Deprecated
- [Deprecated Symbols](./deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## See Also

### Services
- [MIDI System Setup](./midi-system-setup.md)
  Configure the global MIDI system.
- [MIDI Bluetooth](./midi-bluetooth.md)
  Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](./midi-messages.md)
  Create and configure messages.
- [MIDI Thru Connection](./midi-thru-connection.md)
  Create play-through connections between sources and destinations.
- [MIDI Networking](./midi-networking.md)
  Create and manage devices connected over a local network.
- [MIDI Drivers](./midi-drivers.md)
  Create driver plug-ins.
- [MIDI Capability Inquiry](./midi-capability-inquiry.md)
  Provide support for bidirectional discovery and configuration of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midi-services)*