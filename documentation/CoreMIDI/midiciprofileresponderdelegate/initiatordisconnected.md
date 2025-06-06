# initiatorDisconnected(_:)

**Framework**: Core MIDI  
**Kind**: method  
**Required**: Yes

Provides an opportunity to perform an action after the system disconnects the initiator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func initiatorDisconnected(_ initiatorMUID: MIDICIInitiatiorMUID)
```

## Parameters

- `initiatorMUID`: The MIDI-CI initiator identifier.

## See Also

- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](midiciprofileresponderdelegate/connectinitiator(_:with:).md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](midiciprofileresponderdelegate/handledata(for:onchannel:data:).md)
  Processes MIDI data for a profile and channel.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](midiciprofileresponderdelegate/willsetprofile(_:onchannel:enabled:).md)
  Provides an opportunity to perform an action before the system sets the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/initiatordisconnected(_:))*