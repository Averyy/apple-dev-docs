# MIDICIResponder

**Framework**: Core MIDI  
**Kind**: class

An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MIDICIResponder
```

## Topics

### Creating a Responder
- [init(deviceInfo: MIDICIDeviceInfo, profileDelegate: any MIDICIProfileResponderDelegate, profileStates: [MIDICIProfileState], supportProperties: Bool)](midiciresponder/init(deviceinfo:profiledelegate:profilestates:supportproperties:).md)
  Creates a new responder.
### Managing the Life Cycle
- [func start() -> Bool](midiciresponder/start.md)
  Starts receiving initiator requests.
- [func stop()](midiciresponder/stop.md)
  Stops receiving initiator requests and disconnects all connected initiators.
### Setting a Responder Delegate
- [var profileDelegate: any MIDICIProfileResponderDelegate](midiciresponder/profiledelegate.md)
  The profile delegate.
- [protocol MIDICIProfileResponderDelegate](midiciprofileresponderdelegate.md)
  A protocol that defines the methods to respond to MIDI-CI responder life-cycle events.
### Inspecting a Responder
- [typealias MIDICIInitiatiorMUID](midiciinitiatiormuid.md)
  The unique MIDI-CI negotiation identifier to use for a responder connection.
- [var initiators: [MIDICIInitiatiorMUID]](midiciresponder/initiators.md)
  An array of initiators.
- [struct MIDICIDeviceIdentification](midicideviceidentification.md)
  A structure that describes a MIDI-CI device.
- [class MIDICIDeviceInfo](midicideviceinfo.md)
  An object that provides basic information about a MIDI-CI device.
- [var deviceInfo: MIDICIDeviceInfo](midiciresponder/deviceinfo.md)
  The MIDI-CI device’s information.
### Broadcasting Profile Changes
- [func notify(MIDICIProfile, onChannel: MIDIChannelNumber, isEnabled: Bool) -> Bool](midiciresponder/notify(_:onchannel:isenabled:).md)
  Enables or disables a profile and notifies all connected initiators.
- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](midiciresponder/send(_:onchannel:profiledata:).md)
  Sends profile-specific data to all connected initiators.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MIDICIDiscoveryManager](midicidiscoverymanager.md)
  A singleton object that performs systemwide MIDI-CI discovery.
- [class MIDICISession](midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder)*