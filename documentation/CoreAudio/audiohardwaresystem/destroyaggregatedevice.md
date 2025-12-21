# destroyAggregateDevice(_:)

**Framework**: Core Audio  
**Kind**: method

Destroys the aggregate device represented by the given AudioHardwareAggregateDevice.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func destroyAggregateDevice(_ device: AudioHardwareAggregateDevice) throws
```

#### Discussion

The actual destruction of the aggregate device is asynchronous and may take place after the call to this routine has returned.

## Parameters

- `device`: The AudioHardwareAggregateDevice to destroy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/destroyaggregatedevice(_:))*