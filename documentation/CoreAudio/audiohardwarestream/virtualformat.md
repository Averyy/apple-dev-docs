# virtualFormat

**Framework**: Core Audio  
**Kind**: property

An AudioStreamBasicDescription that describes the current data format for the stream. The virtual format refers to the data format in which all IOProcs for the owning device will perform IO transactions.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var virtualFormat: AudioStreamBasicDescription { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarestream/virtualformat)*