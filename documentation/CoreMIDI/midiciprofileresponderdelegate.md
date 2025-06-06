# MIDICIProfileResponderDelegate

**Framework**: Core MIDI  
**Kind**: protocol

A protocol that defines the methods to respond to MIDI-CI responder life-cycle events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MIDICIProfileResponderDelegate : NSObjectProtocol
```

## Topics

### Protocol Methods
- [func connectInitiator(MIDICIInitiatiorMUID, with: MIDICIDeviceInfo) -> Bool](midiciprofileresponderdelegate/connectinitiator(_:with:).md)
  Enables a MIDI-CI initiator to create a session or reject the connection attempt.
- [func handleData(for: MIDICIProfile, onChannel: MIDIChannelNumber, data: Data)](midiciprofileresponderdelegate/handledata(for:onchannel:data:).md)
  Processes MIDI data for a profile and channel.
- [func willSetProfile(MIDICIProfile, onChannel: MIDIChannelNumber, enabled: Bool) -> Bool](midiciprofileresponderdelegate/willsetprofile(_:onchannel:enabled:).md)
  Provides an opportunity to perform an action before the system sets the profile.
- [func initiatorDisconnected(MIDICIInitiatiorMUID)](midiciprofileresponderdelegate/initiatordisconnected(_:).md)
  Provides an opportunity to perform an action after the system disconnects the initiator.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var profileDelegate: any MIDICIProfileResponderDelegate](midiciresponder/profiledelegate.md)
  The profile delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofileresponderdelegate)*