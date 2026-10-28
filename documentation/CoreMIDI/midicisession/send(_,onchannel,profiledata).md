# send(_:onChannel:profileData:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Sends profile-specific data to the MIDI-CI session.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func send(_ profile: MIDICIProfile, onChannel channel: MIDIChannelNumber, profileData profileSpecificData: Data) -> Bool
```

```objc
- (BOOL) sendProfile:(MIDICIProfile *) profile onChannel:(MIDIChannelNumber) channel profileData:(NSData *) profileSpecificData;
```

## Return Value

[`true`](../../Swift/true.md) if the data was successfully sent, otherwise [`false`](../../Swift/false.md).

## Parameters

- `profile`: The MIDI-CI profile.
- `channel`: The MIDI channel number.
- `profileSpecificData`: The profile-specific data to send.

## See Also

### Configuring a Session
- [func profileState(forChannel: MIDIChannelNumber) -> MIDICIProfileState](./profilestate%28forchannel%29.md)
  Returns the profile state for the specified MIDI channel number.
- [func enable(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./enable%28_,onchannel%29.md)
  Performs an asynchronous request to enable a profile for a specific MIDI channel number.
- [func disableProfile(MIDICIProfile, onChannel: MIDIChannelNumber) throws](./disableprofile%28_,onchannel%29.md)
  Performs an asynchronous request to disable a profile for a specific MIDI channel number.
- [typealias MIDICIProfileChangedBlock](../midiciprofilechangedblock.md)
  A block the system calls to indicate it has enabled or disabled a profile.
- [var profileChangedCallback: MIDICIProfileChangedBlock?](./profilechangedcallback.md)
  An optional block the system calls after it enables or disables a profile.
- [typealias MIDICIProfileSpecificDataBlock](../midiciprofilespecificdatablock.md)
  A block the system calls when a MIDI-CI session or responder receives profile-specific data.
- [var profileSpecificDataHandler: MIDICIProfileSpecificDataBlock?](./profilespecificdatahandler.md)
  An optional block the system calls when a device sends profile-specific data to the session.
- [var MIDIChannelsWholePort: MIDIChannelNumber](../midichannelswholeport.md)
  A constant value that indicates to use all channels of the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/send(_:onchannel:profiledata:))*