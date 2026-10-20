# MIDICIProfileResponderDelegate

**Framework**: Core MIDI  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods to respond to MIDI-CI responder life-cycle events.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
protocol MIDICIProfileResponderDelegate : NSObjectProtocol
```

```objc
@protocol MIDICIProfileResponderDelegate <NSObject>
```

## Topics

### Protocol Methods
- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](./midiciprofileresponderdelegate/connectinitiator%28_,with%29.md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](./midiciprofileresponderdelegate/handledata%28for,onchannel,data%29.md)
  Processes MIDI data for a profile and channel.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](./midiciprofileresponderdelegate/willsetprofile%28_,onchannel,enabled%29.md)
  Provides an opportunity to perform an action before the system sets the profile.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](./midiciprofileresponderdelegate/initiatordisconnected%28_%29.md)
  Provides an opportunity to perform an action after the system disconnects the initiator.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting a Responder Delegate
- [var profileDelegate: any MIDICIProfileResponderDelegate](./midiciresponder/profiledelegate.md)
  The profile delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate)*