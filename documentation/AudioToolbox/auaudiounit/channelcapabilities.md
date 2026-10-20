# channelCapabilities

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Expresses valid combinations of input and output channels.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var channelCapabilities: [NSNumber]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSNumber *> * channelCapabilities;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSNumber *> * channelCapabilities;
```

#### Discussion

Array elements are [`NSNumber`](../../Foundation/nsnumber.md) values containing integers.

The array index alternates between input and output counts, in ascending order of input/output channels—for example: [0] = first input count, [1] = first output count, [2] = second input count, [3] = second output count, etc.

Positive array values specify the number of input and/or output channels supported.

Negative array values have particular meanings. An input/output value pair of `(-1, -1)` (i.e. [0] = -1, [1] = -1) indicates that any number of channels are supported, as long as they are the same number for both input and output. An input/output value pair combination of `-1` and `-2` (e.g. [0] = -1, [1] = -2) also indicates that any number of channels are supported, but without the requirement that the input and output counts are the same. A negative value less than `-2` (e.g. [0] = -16) specifies a total number of channels across every bus in that scope, regardless of how many channels are set on any particular bus.

An array value of `0` (e.g. [0] = 0) specifies that the input/output channel is not applicable (though typically only used for input channels).

The table below shows a sample selection of valid input and output channel combinations:

| Array Index | Integer Value | Meaning |
| --- | --- | --- |
| [0] ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) [1] | -1 ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) -1 | First input/output count. ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) Any number of input and output channels, requiring that the numbers match. This is the default case. |
| [2] ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) [3] | -1 ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) -2 | Second input/output count. ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) Any number of input and output channels, without requiring that the numbers match. |
| [4] ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) [5] | 2 ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) 6 | Third input/output count. ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) Exactly two input channels, exactly six output channels. |
| [6] ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) [7] | -1 ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) 2 | Fourth input/output count. ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) Any number of input channels, exactly two output channels. |
| [8] ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) [9] | 0 ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) 1 | Fifth input/output count. ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) No input channels, exactly one output channel. |
| [10] ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) [11] | -4 ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) -8 | Sixth input/output count. ![](https://developer.apple.com/tutorials/images/com.apple.audiotoolbox/spacer.png) Up to four input channels, up to eight output channels. |

This version 3 property is bridged to the version 2 `kAudioUnitProperty_SupportedNumChannels` API.

## See Also

### Configuring the Channel Capabilities
- [var channelMap: [NSNumber]?](./channelmap.md)
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](./profilestate%28forcable,channel%29.md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./enable%28_,cable,onchannel%29.md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](./disableprofile%28_,cable,onchannel%29.md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](./profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/channelcapabilities)*