# profileState(forChannel:)

**Framework**: Core MIDI  
**Kind**: method

Returns the profile state for the specified MIDI channel number.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func profileState(forChannel channel: MIDIChannelNumber) -> MIDICIProfileState
```

#### Return Value

A profile state object.

## Parameters

- `channel`: The MIDI channel for which you return the profile state.

## See Also

- [func enable(MIDICIProfile, onChannel: MIDIChannelNumber) throws](midicisession/enable(_:onchannel:).md)
  Performs an asynchronous request to enable a profile for a specific MIDI channel number.
- [func disableProfile(MIDICIProfile, onChannel: MIDIChannelNumber) throws](midicisession/disableprofile(_:onchannel:).md)
  Performs an asynchronous request to disable a profile for a specific MIDI channel number.
- [typealias MIDICIProfileChangedBlock](midiciprofilechangedblock.md)
  A block the system calls to indicate it has enabled or disabled a profile.
- [var profileChangedCallback: MIDICIProfileChangedBlock?](midicisession/profilechangedcallback.md)
  An optional block the system calls after it enables or disables a profile.
- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](midicisession/send(_:onchannel:profiledata:).md)
  Sends profile-specific data to the MIDI-CI session.
- [typealias MIDICIProfileSpecificDataBlock](midiciprofilespecificdatablock.md)
  A block the system calls when a MIDI-CI session or responder receives profile-specific data.
- [var profileSpecificDataHandler: MIDICIProfileSpecificDataBlock?](midicisession/profilespecificdatahandler.md)
  An optional block the system calls when a device sends profile-specific data to the session.
- [let MIDIChannelsWholePort: MIDIChannelNumber](midichannelswholeport.md)
  A constant value that indicates to use all channels of the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/profilestate(forchannel:))*