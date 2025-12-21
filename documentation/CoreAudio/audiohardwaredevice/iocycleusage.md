# ioCycleUsage

**Framework**: Core Audio  
**Kind**: property

A Float whose range is from 0 to 1. This value indicates how much of the client portion of the IO cycle the process will use.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var ioCycleUsage: Float { get throws }
```

#### Discussion

The client portion of the IO cycle is the portion of the cycle in which the device calls the IOProcs so this property does not the apply to the duration of the entire cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/iocycleusage)*