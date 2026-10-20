# MIDICIProfileChangedBlock

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A block the system calls to indicate it has enabled or disabled a profile.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
typealias MIDICIProfileChangedBlock = (MIDICISession, MIDIChannelNumber, MIDICIProfile, Bool) -> Void
```

```c
typedef void (^)(MIDICISession *, unsigned char, MIDICIProfile *, _Bool) MIDICIProfileChangedBlock;
```

## Parameters

- `session`: The MIDI-CI session.
- `channel`: The MIDI channel number.
- `profile`: The profile the system enabled or disabled.
- `enabled`: A Boolean value that indicates whether the system enabled the profile.

## See Also

### Configuring a Session
- [func profileState(forChannel: MIDIChannelNumber) -> MIDICIProfileState](./midicisession/profilestate%28forchannel%29.md)
  Returns the profile state for the specified MIDI channel number.
- [func enable(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./midicisession/enable%28_,onchannel%29.md)
  Performs an asynchronous request to enable a profile for a specific MIDI channel number.
- [func disableProfile(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./midicisession/disableprofile%28_,onchannel%29.md)
  Performs an asynchronous request to disable a profile for a specific MIDI channel number.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilechangedblock)*