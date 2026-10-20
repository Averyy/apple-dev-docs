# disableProfile(_:cable:onChannel:)

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
func disableProfile(_ profile: MIDICIProfile, cable: UInt8, onChannel channel: MIDIChannelNumber) throws
```

```objc
- (BOOL) disableProfile:(MIDICIProfile *) profile cable:(uint8_t) cable onChannel:(MIDIChannelNumber) channel error:(NSError **) outError;
```

## See Also

### Configuring the Channel Capabilities
- [var channelCapabilities: [NSNumber]?](./channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [var channelMap: [NSNumber]?](./channelmap.md)
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](./profilestate%28forcable,channel%29.md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./enable%28_,cable,onchannel%29.md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](./profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/disableprofile(_:cable:onchannel:))*