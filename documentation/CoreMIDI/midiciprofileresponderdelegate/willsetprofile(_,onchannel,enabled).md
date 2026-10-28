# willSetProfile(_:onChannel:enabled:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to perform an action before the system sets the profile.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
optional func willSetProfile(_ aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, enabled shouldEnable: Bool) -> Bool
```

```objc
- (BOOL) willSetProfile:(MIDICIProfile *) aProfile onChannel:(MIDIChannelNumber) channel enabled:(BOOL) shouldEnable;
```

## Return Value

A Boolean value that indicates whether the system enabled the profile.

## Parameters

- `aProfile`: The profile the system uses to configure the device.
- `channel`: The MIDI channel assignment.
- `shouldEnable`: A Booean value that indicates whether the system should enable the profile.

## See Also

### Protocol Methods
- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](./connectinitiator%28_,with%29.md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](./handledata%28for,onchannel,data%29.md)
  Processes MIDI data for a profile and channel.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](./initiatordisconnected%28_%29.md)
  Provides an opportunity to perform an action after the system disconnects the initiator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/willsetprofile(_:onchannel:enabled:))*