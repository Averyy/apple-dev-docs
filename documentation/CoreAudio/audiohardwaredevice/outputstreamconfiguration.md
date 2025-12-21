# outputStreamConfiguration

**Framework**: Core Audio  
**Kind**: property

This property returns the stream configuration of the device in an array of AudioBuffers (with the buffer data set to nil) which describes the list of streams and the number of channels in each stream. This corresponds to what will be passed into the IOProc.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var outputStreamConfiguration: [AudioBuffer] { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/outputstreamconfiguration)*