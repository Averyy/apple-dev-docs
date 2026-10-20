# profileState(forCable:channel:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func profileState(forCable cable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState
```

```objc
- (MIDICIProfileState *) profileStateForCable:(uint8_t) cable channel:(MIDIChannelNumber) channel;
```

## See Also

### Configuring the Channel Capabilities
- [var channelCapabilities: [NSNumber]?](./channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [var channelMap: [NSNumber]?](./channelmap.md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./enable%28_,cable,onchannel%29.md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./disableprofile%28_,cable,onchannel%29.md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](./profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/profilestate(forcable:channel:))*