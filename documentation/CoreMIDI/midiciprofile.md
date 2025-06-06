# MIDICIProfile

**Framework**: Core MIDI  
**Kind**: class

A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
class MIDICIProfile
```

## Topics

### Creating a Profile
- [init(data: Data)](midiciprofile/init(data:).md)
  Creates a MIDI profile for the specified data.
- [init(data: Data, name: String)](midiciprofile/init(data:name:).md)
  Creates a named MIDI profile for the specified data.
### Inspecting a Profile
- [var name: String](midiciprofile/name.md)
  A string that describes the profile.
- [var profileID: Data](midiciprofile/profileid.md)
  The unique five-byte profile identifier that represents the profile.

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
- [class MIDICIProfileState](midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [class MIDICIResponder](midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofile)*