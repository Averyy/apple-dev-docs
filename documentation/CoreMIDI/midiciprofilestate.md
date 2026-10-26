# MIDICIProfileState

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
class MIDICIProfileState
```

```objc
@interface MIDICIProfileState : NSObject
```

## Topics

### Creating a Profile State
- [init(channel: MIDIChannelNumber, enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](./midiciprofilestate/init%28channel,enabledprofiles,disabledprofiles%29.md)
  Creates a new profile state object for the specified MIDI channel and profiles.
- [init(enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](./midiciprofilestate/init%28enabledprofiles,disabledprofiles%29.md)
  Creates a new profile state object for the specified profiles.
### Accessing the MIDI Channel
- [var midiChannel: MIDIChannelNumber](./midiciprofilestate/midichannel.md)
  The MIDI channel to which this state applies.
### Accessing Profiles
- [var enabledProfiles: [MIDICIProfile]](./midiciprofilestate/enabledprofiles.md)
  The object’s enabled profiles.
- [var disabledProfiles: [MIDICIProfile]](./midiciprofilestate/disabledprofiles.md)
  The object’s disabled profiles.
### Initializers
- [init?(coder: NSCoder)](./midiciprofilestate/init%28coder%29.md)

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

### Capability Inquiry
- [class MIDICIDiscoveryManager](./midicidiscoverymanager.md)
  A singleton object that performs systemwide MIDI-CI discovery.
- [class MIDICISession](./midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](./midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIResponder](./midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.
- [MIDICIProfileStateList](./midiciprofilestatelist.md)
  An array of profile state objects that describes the profile configuration for all channels of a reachable MIDI-CI node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestate)*