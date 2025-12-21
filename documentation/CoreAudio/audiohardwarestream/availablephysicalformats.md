# availablePhysicalFormats

**Framework**: Core Audio  
**Kind**: property

An array of AudioStreamRangedDescriptions that describe the available data formats for the stream. The physical format refers to the data format in which the hardware for the owning device performs its IO transactions.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var availablePhysicalFormats: [AudioStreamRangedDescription] { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarestream/availablephysicalformats)*