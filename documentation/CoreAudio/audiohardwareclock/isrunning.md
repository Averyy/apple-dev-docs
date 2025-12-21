# isRunning

**Framework**: Core Audio  
**Kind**: property

A Bool where a value of false indicates the device is not providing timestamps and a value of true means that it is.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var isRunning: Bool { get throws }
```

#### Discussion

The notification for this property is usually sent from the device’s IO thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareclock/isrunning)*