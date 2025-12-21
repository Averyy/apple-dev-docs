# volumeDecibelValue

**Framework**: Core Audio  
**Kind**: property

A Float that represents the value of the volume control in dB.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var volumeDecibelValue: Float { get throws }
```

#### Discussion

Note that the set of all Float values in the dB range for the control is much larger than the set of actual values that the hardware can select. This means that the Float range has a many to one mapping with the underlying hardware values. As such, setting a dB value will result in the control taking on the value nearest to what was set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarecontrol/volumedecibelvalue)*