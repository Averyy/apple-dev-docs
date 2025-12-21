# setAllowsSleeping(_:)

**Framework**: Core Audio  
**Kind**: method

Set the allowsSleeping property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func setAllowsSleeping(_ allowed: Bool) throws
```

## Parameters

- `allowed`: A Bool where true indicates that the process will allow the CPU to   idle sleep even if there is audio IO in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/setallowssleeping(_:))*