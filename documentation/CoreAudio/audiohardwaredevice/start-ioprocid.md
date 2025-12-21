# start(IOProcID:)

**Framework**: Core Audio  
**Kind**: method

Starts IO for the given AudioDeviceIOProcID.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func start(IOProcID: AudioDeviceIOProcID? = nil) throws
```

#### Discussion

IOProcIDs should be written in C to ensure realtime safety. IOProcIDs can be registered on the device with AudioDeviceCreateIOProcID or AudioDeviceCreateIOProcIDWithBlock from AudioHardware.h.

## Parameters

- `IOProcID`: The AudioDeviceIOProcID to start. Note that this can be nil, which   starts the hardware regardless of whether or not there are any IOProcs registered. This is   necessary if any of the device’s timing services are to be used. A balancing call to   stop with a nil IOProcID is required to stop the hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/start(ioprocid:))*