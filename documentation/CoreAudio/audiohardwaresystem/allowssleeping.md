# allowsSleeping

**Framework**: Core Audio  
**Kind**: property

A Bool where true indicates that the process will allow the CPU to idle sleep even if there is audio IO in progress. Fasle indicates that the CPU will not be allowed to idle sleep.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var allowsSleeping: Bool { get throws }
```

#### Discussion

Note that this property won’t affect when the CPU is forced to sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/allowssleeping)*