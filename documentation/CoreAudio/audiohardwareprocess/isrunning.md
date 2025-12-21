# isRunning

**Framework**: Core Audio  
**Kind**: property

A Bool where a value of true indicates that there is audio IO in progress in the process.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var isRunning: Bool { get throws }
```

#### Discussion

Note that audio IO may be in progress even if no input or output streams are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareprocess/isrunning)*