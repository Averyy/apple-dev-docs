# handleData(for:onChannel:data:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Processes MIDI data for a profile and channel.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
optional func handleData(for aProfile: MIDICIProfile, onChannel channel: MIDIChannelNumber, data inData: Data)
```

```objc
- (void) handleDataForProfile:(MIDICIProfile *) aProfile onChannel:(MIDIChannelNumber) channel data:(NSData *) inData;
```

## Parameters

- `aProfile`: The MIDI-CI profile.
- `channel`: The MIDI channel.
- `inData`: The data to process.

## See Also

### Protocol Methods
- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](./connectinitiator%28_,with%29.md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](./willsetprofile%28_,onchannel,enabled%29.md)
  Provides an opportunity to perform an action before the system sets the profile.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](./initiatordisconnected%28_%29.md)
  Provides an opportunity to perform an action after the system disconnects the initiator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate/handledata(for:onchannel:data:))*