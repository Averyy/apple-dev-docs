# setIsProcessInputMuted(_:)

**Framework**: Core Audio  
**Kind**: method

Set the isProcessInputMuted property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func setIsProcessInputMuted(_ muted: Bool) throws
```

#### Discussion

This property does not apply to aggregate devices, just real, physical devices.

## Parameters

- `muted`: A Bool where true indicates that the current process’s audio will be   zeroed out by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/setisprocessinputmuted(_:))*