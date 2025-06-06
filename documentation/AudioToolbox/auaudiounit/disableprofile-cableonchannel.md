# disableProfile(_:cable:onChannel:)

**Framework**: Audio Toolbox  
**Kind**: method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func disableProfile(_ profile: MIDICIProfile, cable: UInt8, onChannel channel: MIDIChannelNumber) throws
```

## See Also

- [var channelCapabilities: [NSNumber]?](auaudiounit/channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [var channelMap: [NSNumber]?](auaudiounit/channelmap.md)
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](auaudiounit/profilestate(forcable:channel:).md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/enable(_:cable:onchannel:).md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](auaudiounit/profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/disableprofile(_:cable:onchannel:))*