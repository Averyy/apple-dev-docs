# makeAggregateDevice(description:)

**Framework**: Core Audio  
**Kind**: method

Creates a new aggregate device  using the provided description.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func makeAggregateDevice(description: [String : Any]) throws -> AudioHardwareAggregateDevice?
```

#### Return Value

An AudioHardwareAggregateDevice representing the newly created aggregate device.

## Parameters

- `description`: The Dictionary that specifies how to build the aggregate device.   The supported keys are described in the AudioAggregateDevice Constants section of   AudioHardware.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/makeaggregatedevice(description:))*