# profileState(forChannel:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Returns the profile state for the specified MIDI channel number.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
func profileState(forChannel channel: MIDIChannelNumber) -> MIDICIProfileState
```

```objc
- (MIDICIProfileState *) profileStateForChannel:(MIDIChannelNumber) channel;
```

## Return Value

A profile state object.

## Parameters

- `channel`: The MIDI channel for which you return the profile state.

## See Also

### Configuring a Session
- [func enable(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./enable%28_,onchannel%29.md)
  Performs an asynchronous request to enable a profile for a specific MIDI channel number.
- [func disableProfile(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./disableprofile%28_,onchannel%29.md)
  Performs an asynchronous request to disable a profile for a specific MIDI channel number.
- [typealias MIDICIProfileChangedBlock](../midiciprofilechangedblock.md)
  A block the system calls to indicate it has enabled or disabled a profile.
- [var profileChangedCallback: MIDICIProfileChangedBlock?](./profilechangedcallback.md)
  An optional block the system calls after it enables or disables a profile.
- [func send(MIDICIProfile, onChannel: MIDIChannelNumber, profileData: Data) -> Bool](./send%28_,onchannel,profiledata%29.md)
  Sends profile-specific data to the MIDI-CI session.
- [typealias MIDICIProfileSpecificDataBlock](../midiciprofilespecificdatablock.md)
  A block the system calls when a MIDI-CI session or responder receives profile-specific data.
- [var profileSpecificDataHandler: MIDICIProfileSpecificDataBlock?](./profilespecificdatahandler.md)
  An optional block the system calls when a device sends profile-specific data to the session.
- [var MIDIChannelsWholePort: MIDIChannelNumber](../midichannelswholeport.md)
  A constant value that indicates to use all channels of the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/profilestate(forchannel:))*