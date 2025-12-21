# setPreferredOutputChannelsForStereo(_:)

**Framework**: Core Audio  
**Kind**: method

Set the preferredOutputChannelsForStereo property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func setPreferredOutputChannelsForStereo(_ channels: [UInt32]) throws
```

#### Discussion

There are no restrictions on the channel numbers that can be used.

## Parameters

- `channels`: An array of two UInt32s, the first for the left channel, the second   for the right channel, that indicate the channel numbers to use for stereo output IO on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/setpreferredoutputchannelsforstereo(_:))*