# setAllowsUnloading(_:)

**Framework**: Core Audio  
**Kind**: method

Set the allowsUnloading property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func setAllowsUnloading(_ allowed: Bool) throws
```

## Parameters

- `allowed`: A Bool where true indicates that this process wants the HAL to unload   itself after a period of inactivity where there are no IOProcs and no listeners registered with any object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/setallowsunloading(_:))*