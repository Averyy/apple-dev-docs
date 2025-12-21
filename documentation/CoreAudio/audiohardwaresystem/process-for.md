# process(for:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func process(for PID: pid_t) throws -> AudioHardwareProcess?
```

#### Return Value

The AudioHardwareProcess that corresponds with the given PID, or nil if the PID does not correspond with any process object.

## Parameters

- `PID`: A pid_t representing the PID of the process object to obtain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/process(for:))*