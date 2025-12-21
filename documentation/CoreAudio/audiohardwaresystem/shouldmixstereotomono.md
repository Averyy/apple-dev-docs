# shouldMixStereoToMono

**Framework**: Core Audio  
**Kind**: property

A Bool where a value of true indicates that devices should mix stereo signals down to mono.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var shouldMixStereoToMono: Bool { get throws }
```

#### Discussion

The two channels on the device that comprise the stereo signal are defined on the AudioHardwareDevice by preferredChannelsForStereo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/shouldmixstereotomono)*