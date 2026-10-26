# MIDICISession

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

An object that represents a MIDI-CI session.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
class MIDICISession
```

```objc
@interface MIDICISession : NSObject
```

#### Overview

A MIDI-CI session is a bidirectional communication path between a MIDI source and destination identified using MIDI-CI discovery. Use a session to manipulate MIDI-CI profiles and to discover device capabilities.

## Topics

### Creating a Session
- [init(discoveredNode: MIDICIDiscoveredNode, dataReadyHandler: () -> Void, disconnectHandler: MIDICISessionDisconnectBlock)](./midicisession/init%28discoverednode,datareadyhandler,disconnecthandler%29.md)
  Creates a MIDI-CI session.
### Configuring a Session
- [func profileState(forChannel: MIDIChannelNumber) -> MIDICIProfileState](./midicisession/profilestate%28forchannel%29.md)
  Returns the profile state for the specified MIDI channel number.
- [func enable(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./midicisession/enable%28_,onchannel%29.md)
  Performs an asynchronous request to enable a profile for a specific MIDI channel number.
- [func disableProfile(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./midicisession/disableprofile%28_,onchannel%29.md)
  Performs an asynchronous request to disable a profile for a specific MIDI channel number.
- [typealias MIDICIProfileChangedBlock](./midiciprofilechangedblock.md)
  A block the system calls to indicate it has enabled or disabled a profile.
- [var profileChangedCallback: MIDICIProfileChangedBlock?](./midicisession/profilechangedcallback.md)
  An optional block the system calls after it enables or disables a profile.
- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](./midicisession/send%28_,onchannel,profiledata%29.md)
  Sends profile-specific data to the MIDI-CI session.
- [typealias MIDICIProfileSpecificDataBlock](./midiciprofilespecificdatablock.md)
  A block the system calls when a MIDI-CI session or responder receives profile-specific data.
- [var profileSpecificDataHandler: MIDICIProfileSpecificDataBlock?](./midicisession/profilespecificdatahandler.md)
  An optional block the system calls when a device sends profile-specific data to the session.
- [var MIDIChannelsWholePort: MIDIChannelNumber](./midichannelswholeport.md)
  A constant value that indicates to use all channels of the port.
### Inspecting a Session
- [var deviceInfo: MIDICIDeviceInfo](./midicisession/deviceinfo.md)
  Information about a MIDI-CI device.
- [var maxSysExSize: NSNumber](./midicisession/maxsysexsize.md)
  The maximum size of System Exclusive (SysEx) messages.
- [var midiDestination: MIDIEntityRef](./midicisession/mididestination.md)
  The MIDI destination with which the session is communicating.
- [var maxPropertyRequests: NSNumber](./midicisession/maxpropertyrequests.md)
  The maximum number of simultaneous property exchange requests, if supported.
- [var supportsProfileCapability: Bool](./midicisession/supportsprofilecapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI profile’s capability.
- [var supportsPropertyCapability: Bool](./midicisession/supportspropertycapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI property exchange capability.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Capability Inquiry
- [class MIDICIDiscoveryManager](./midicidiscoverymanager.md)
  A singleton object that performs systemwide MIDI-CI discovery.
- [class MIDICIProfile](./midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](./midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [class MIDICIResponder](./midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.
- [MIDICIProfileStateList](./midiciprofilestatelist.md)
  An array of profile state objects that describes the profile configuration for all channels of a reachable MIDI-CI node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession)*