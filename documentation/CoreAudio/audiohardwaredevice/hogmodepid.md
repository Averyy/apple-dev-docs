# hogModePID

**Framework**: Core Audio  
**Kind**: property

A pid_t indicating the process that currently owns exclusive access to the device or a value of -1 indicating that the device is currently available to all processes.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var hogModePID: pid_t { get throws }
```

#### Discussion

If the device is in a non-mixable mode, the HAL will automatically take hog mode on behalf of the first process to start an IOProc.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/hogmodepid)*