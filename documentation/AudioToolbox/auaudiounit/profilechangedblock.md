# profileChangedBlock

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var profileChangedBlock: AUMIDICIProfileChangedBlock? { get set }
```

```objc
@property (nonatomic, nullable) AUMIDICIProfileChangedBlock profileChangedBlock;
```

## See Also

### Configuring the Channel Capabilities
- [var channelCapabilities: [NSNumber]?](./channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [var channelMap: [NSNumber]?](./channelmap.md)
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](./profilestate%28forcable,channel%29.md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./enable%28_,cable,onchannel%29.md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./disableprofile%28_,cable,onchannel%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/profilechangedblock)*