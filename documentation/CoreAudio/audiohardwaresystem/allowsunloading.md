# allowsUnloading

**Framework**: Core Audio  
**Kind**: property

A Bool where true indicates that this process wants the HAL to unload itself after a period of inactivity where there are no IOProcs and no listeners registered with any object.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var allowsUnloading: Bool { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/allowsunloading)*