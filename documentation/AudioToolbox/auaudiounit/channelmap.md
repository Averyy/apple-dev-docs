# channelMap

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) NSArray<NSNumber *> * channelMap;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSArray<NSNumber *> * channelMap;
```

## See Also

### Configuring the Channel Capabilities
- [var channelCapabilities: [NSNumber]?](./channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](./profilestate%28forcable,channel%29.md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./enable%28_,cable,onchannel%29.md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./disableprofile%28_,cable,onchannel%29.md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](./profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/channelmap)*