# MIDICIResponder

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
class MIDICIResponder
```

```objc
@interface MIDICIResponder : NSObject
```

## Topics

### Creating a Responder
- [init(deviceInfo: MIDICIDeviceInfo, profileDelegate: any MIDICIProfileResponderDelegate, profileStates: [MIDICIProfileState], supportProperties: Bool)](./midiciresponder/init%28deviceinfo,profiledelegate,profilestates,supportproperties%29.md)
  Creates a new responder.
### Managing the Life Cycle
- [func start() -> Bool](./midiciresponder/start%28%29.md)
  Starts receiving initiator requests.
- [func stop()](./midiciresponder/stop%28%29.md)
  Stops receiving initiator requests and disconnects all connected initiators.
### Setting a Responder Delegate
- [var profileDelegate: any MIDICIProfileResponderDelegate](./midiciresponder/profiledelegate.md)
  The profile delegate.
- [protocol MIDICIProfileResponderDelegate](./midiciprofileresponderdelegate.md)
  A protocol that defines the methods to respond to MIDI-CI responder life-cycle events.
### Inspecting a Responder
- [typealias MIDICIInitiatiorMUID](./midiciinitiatiormuid.md)
  The unique MIDI-CI negotiation identifier to use for a responder connection.
- [var initiators: [MIDICIInitiatiorMUID]](./midiciresponder/initiators.md)
  An array of initiators.
- [struct MIDICIDeviceIdentification](./midicideviceidentification.md)
  A structure that describes a MIDI-CI device.
- [class MIDICIDeviceInfo](./midicideviceinfo.md)
  An object that provides basic information about a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](./midiciresponder/deviceinfo.md)
  The MIDI-CI device’s information.
### Broadcasting Profile Changes
- [func notify(MIDICIProfile, onChannel: MIDIChannelNumber, isEnabled: Bool) -> Bool](./midiciresponder/notify%28_,onchannel,isenabled%29.md)
  Enables or disables a profile and notifies all connected initiators.
- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](./midiciresponder/send%28_,onchannel,profiledata%29.md)
  Sends profile-specific data to all connected initiators.

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
- [class MIDICISession](./midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](./midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](./midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [MIDICIProfileStateList](./midiciprofilestatelist.md)
  An array of profile state objects that describes the profile configuration for all channels of a reachable MIDI-CI node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder)*