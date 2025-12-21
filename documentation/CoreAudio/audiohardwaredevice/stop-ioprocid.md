# stop(IOProcID:)

**Framework**: Core Audio  
**Kind**: method

Stops IO for the given AudioDeviceIOProcID.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func stop(IOProcID: AudioDeviceIOProcID? = nil) throws
```

## Parameters

- `IOProcID`: The AudioDeviceIOProcID to stop. This can be nil to stop the   hardware if a call to start was made with a nil IOProcID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/stop(ioprocid:))*