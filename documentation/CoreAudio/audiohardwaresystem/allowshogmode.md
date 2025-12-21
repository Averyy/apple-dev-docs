# allowsHogMode

**Framework**: Core Audio  
**Kind**: property

A Bool where true indicates that this process wants the HAL to automatically take hog mode and false indicates that the HAL should not automatically take hog mode on behalf of the process.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var allowsHogMode: Bool { get throws }
```

#### Discussion

Processes that only ever use the default device are the sort that should set this property’s value to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/allowshogmode)*