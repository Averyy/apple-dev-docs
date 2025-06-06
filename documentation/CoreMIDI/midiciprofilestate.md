# MIDICIProfileState

**Framework**: Core MIDI  
**Kind**: class

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

## Topics

### Creating a Profile State
- [init(channel: MIDIChannelNumber, enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](midiciprofilestate/init(channel:enabledprofiles:disabledprofiles:).md)
  Creates a new profile state object for the specified MIDI channel and profiles.
- [init(enabledProfiles: [MIDICIProfile], disabledProfiles: [MIDICIProfile])](midiciprofilestate/init(enabledprofiles:disabledprofiles:).md)
  Creates a new profile state object for the specified profiles.
### Accessing the MIDI Channel
- [var midiChannel: MIDIChannelNumber](midiciprofilestate/midichannel.md)
  The MIDI channel to which this state applies.
### Accessing Profiles
- [var enabledProfiles: [MIDICIProfile]](midiciprofilestate/enabledprofiles.md)
  The object’s enabled profiles.
- [var disabledProfiles: [MIDICIProfile]](midiciprofilestate/disabledprofiles.md)
  The object’s disabled profiles.

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

- [class MIDICIDiscoveryManager](midicidiscoverymanager.md)
  A singleton object that performs systemwide MIDI-CI discovery.
- [class MIDICISession](midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIResponder](midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestate)*