# connectInitiator(_:with:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Enables a MIDI-CI initiator to create a session or reject the connection attempt.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
func connectInitiator(_ initiatorMUID: MIDICIInitiatiorMUID, with deviceInfo: MIDICIDeviceInfo) -> Bool
```

```objc
- (BOOL) connectInitiator:(MIDICIInitiatiorMUID) initiatorMUID withDeviceInfo:(MIDICIDeviceInfo *) deviceInfo;
```

## Parameters

- `initiatorMUID`: The ID of the MIDI-CI initiator.
- `deviceInfo`: The information that describes a device.

## See Also

### Protocol Methods
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](./handledata%28for,onchannel,data%29.md)
  Processes MIDI data for a profile and channel.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](./willsetprofile%28_,onchannel,enabled%29.md)
  Provides an opportunity to perform an action before the system sets the profile.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](./initiatordisconnected%28_%29.md)
  Provides an opportunity to perform an action after the system disconnects the initiator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/connectinitiator(_:with:))*