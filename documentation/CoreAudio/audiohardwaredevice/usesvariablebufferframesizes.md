# usesVariableBufferFrameSizes

**Framework**: Core Audio  
**Kind**: property

A Bool where true indicates that the sizes of the buffers passed to an IOProc will vary by a small amount.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var usesVariableBufferFrameSizes: Bool { get throws }
```

#### Discussion

largestVariableBufferFrameSize will indicate the largest buffer that will be passed and bufferFrameSize will indicate the smallest buffer that will get passed to the IOProc. The usage of this property is narrowed to only allow for devices whose buffer sizes vary by small amounts greater than bufferFrameSize. It is not intended to be a license for devices to be able to send buffers however they please. Rather, it is intended to allow for hardware whose natural rhythms lead to this necessity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/usesvariablebufferframesizes)*