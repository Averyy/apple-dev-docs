# connectInitiator(_:with:)

**Framework**: Core MIDI  
**Kind**: method  
**Required**: Yes

Enables a MIDI-CI initiator to create a session or reject the connection attempt.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func connectInitiator(_ initiatorMUID: MIDICIInitiatiorMUID, with deviceInfo: MIDICIDeviceInfo) -> Bool
```

## Parameters

- `initiatorMUID`: The ID of the MIDI-CI initiator.
- `deviceInfo`: The information that describes a device.

## See Also

- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](midiciprofileresponderdelegate/handledata(for:onchannel:data:).md)
  Processes MIDI data for a profile and channel.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](midiciprofileresponderdelegate/willsetprofile(_:onchannel:enabled:).md)
  Provides an opportunity to perform an action before the system sets the profile.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](midiciprofileresponderdelegate/initiatordisconnected(_:).md)
  Provides an opportunity to perform an action after the system disconnects the initiator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/connectinitiator(_:with:))*