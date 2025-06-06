# channelMap

**Framework**: Audio Toolbox  
**Kind**: property

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var channelMap: [NSNumber]? { get set }
```

## See Also

- [var channelCapabilities: [NSNumber]?](auaudiounit/channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](auaudiounit/profilestate(forcable:channel:).md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/enable(_:cable:onchannel:).md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/disableprofile(_:cable:onchannel:).md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](auaudiounit/profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/channelmap)*