# initiatorDisconnected(_:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an opportunity to perform an action after the system disconnects the initiator.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
func initiatorDisconnected(_ initiatorMUID: MIDICIInitiatiorMUID)
```

```objc
- (void) initiatorDisconnected:(MIDICIInitiatiorMUID) initiatorMUID;
```

## Parameters

- `initiatorMUID`: The MIDI-CI initiator identifier.

## See Also

### Protocol Methods
- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](./connectinitiator%28_,with%29.md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](./handledata%28for,onchannel,data%29.md)
  Processes MIDI data for a profile and channel.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](./willsetprofile%28_,onchannel,enabled%29.md)
  Provides an opportunity to perform an action before the system sets the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/initiatordisconnected(_:))*