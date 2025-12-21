# availableVirtualFormats

**Framework**: Core Audio  
**Kind**: property

An array of AudioStreamRangedDescriptions that describe the available data formats for the stream. The virtual format refers to the data format in which all IOProcs for the owning device will perform IO transactions.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var availableVirtualFormats: [AudioStreamRangedDescription] { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarestream/availablevirtualformats)*