# start(at:flags:IOProcID:)

**Framework**: Core Audio  
**Kind**: method

Starts IO for the given AudioDeviceIOProcID and aligns the IO cycle of the device with the given time.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func start(at time: AudioTimeStamp, flags: UInt32 = 0, IOProcID: AudioDeviceIOProcID? = nil) throws -> AudioTimeStamp?
```

#### Return Value

An AudioTimeStamp containing the actual time the IOProc will start if the call is successful.

#### Discussion

An AudioHardwareError of kAudioHardwareUnsupportedOperationError will be thrown if the device does not support starting at a specific time. IOProcs should be written in C to ensure realtime safety. IOProcIDs can be registered on the device with AudioDeviceCreateIOProcID or AudioDeviceCreateIOProcIDWithBlock from AudioHardware.h.

## Parameters

- `time`: An AudioTimeStamp that containing the requested time to start the IOProc.
- `flags`: A UInt32 containing flags that modify how this function behaves.
- `IOProcID`: The AudioDeviceIOProcID to start. Note that this can be nil, which starts   the hardware regardless of whether or not there are any IOProcs registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/start(at:flags:ioprocid:))*