# isProcessInputMuted

**Framework**: Core Audio  
**Kind**: property

A Bool where true indicates that the current process’s input audio will be zeroed out by the system.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var isProcessInputMuted: Bool { get throws }
```

#### Discussion

This property does not apply to aggregate devices, just real, physical devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/isprocessinputmuted)*