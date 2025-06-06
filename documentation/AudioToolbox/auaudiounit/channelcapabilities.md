# channelCapabilities

**Framework**: Audio Toolbox  
**Kind**: property

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

#### Discussion

Array elements are [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) values containing integers.

The array index alternates between input and output counts, in ascending order of input/output channels—for example: [0] = first input count, [1] = first output count, [2] = second input count, [3] = second output count, etc.

Positive array values specify the number of input and/or output channels supported.

Negative array values have particular meanings. An input/output value pair of `(-1, -1)` (i.e. [0] = -1, [1] = -1) indicates that any number of channels are supported, as long as they are the same number for both input and output. An input/output value pair combination of `-1` and `-2` (e.g. [0] = -1, [1] = -2) also indicates that any number of channels are supported, but without the requirement that the input and output counts are the same. A negative value less than `-2` (e.g. [0] = -16) specifies a total number of channels across every bus in that scope, regardless of how many channels are set on any particular bus.

An array value of `0` (e.g. [0] = 0) specifies that the input/output channel is not applicable (though typically only used for input channels).

The table below shows a sample selection of valid input and output channel combinations:

| Array Index | Integer Value | Meaning |
| --- | --- | --- |
| [0] ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [1] | -1 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) -1 | First input/output count. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Any number of input and output channels, requiring that the numbers match. This is the default case. |
| [2] ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [3] | -1 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) -2 | Second input/output count. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Any number of input and output channels, without requiring that the numbers match. |
| [4] ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [5] | 2 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 6 | Third input/output count. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Exactly two input channels, exactly six output channels. |
| [6] ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [7] | -1 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 2 | Fourth input/output count. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Any number of input channels, exactly two output channels. |
| [8] ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [9] | 0 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 | Fifth input/output count. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) No input channels, exactly one output channel. |
| [10] ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [11] | -4 ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) -8 | Sixth input/output count. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Up to four input channels, up to eight output channels. |

This version 3 property is bridged to the version 2 `kAudioUnitProperty_SupportedNumChannels` API.

## See Also

- [var channelMap: [NSNumber]?](auaudiounit/channelmap.md)
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](auaudiounit/profilestate(forcable:channel:).md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/enable(_:cable:onchannel:).md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/disableprofile(_:cable:onchannel:).md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](auaudiounit/profilechangedblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/channelcapabilities)*