# handleData(for:onChannel:data:)

**Framework**: Core MIDI  
**Kind**: method

Processes MIDI data for a profile and channel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func handleData(for aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, data inData: Data)
```

## Parameters

- `aProfile`: The MIDI-CI profile.
- `channel`: The MIDI channel.
- `inData`: The data to process.

## See Also

- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](midiciprofileresponderdelegate/connectinitiator(_:with:).md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](midiciprofileresponderdelegate/willsetprofile(_:onchannel:enabled:).md)
  Provides an opportunity to perform an action before the system sets the profile.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](midiciprofileresponderdelegate/initiatordisconnected(_:).md)
  Provides an opportunity to perform an action after the system disconnects the initiator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/handledata(for:onchannel:data:))*