# willSetProfile(_:onChannel:enabled:)

**Framework**: Core MIDI  
**Kind**: method

Provides an opportunity to perform an action before the system sets the profile.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func willSetProfile(_ aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, enabled shouldEnable: Bool) -> Bool
```

#### Return Value

A Boolean value that indicates whether the system enabled the profile.

## Parameters

- `aProfile`: The profile the system uses to configure the device.
- `channel`: The MIDI channel assignment.
- `shouldEnable`: A Booean value that indicates whether the system should enable the profile.

## See Also

- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](midiciprofileresponderdelegate/connectinitiator(_:with:).md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](midiciprofileresponderdelegate/handledata(for:onchannel:data:).md)
  Processes MIDI data for a profile and channel.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](midiciprofileresponderdelegate/initiatordisconnected(_:).md)
  Provides an opportunity to perform an action after the system disconnects the initiator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/willsetprofile(_:onchannel:enabled:))*