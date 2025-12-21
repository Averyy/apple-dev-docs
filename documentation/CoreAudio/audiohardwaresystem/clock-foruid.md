# clock(forUID:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func clock(forUID UID: String) throws -> AudioHardwareClock?
```

#### Return Value

The AudioHardwareClock that corresponds with the given UID, or nil if the UID does not correspond with any clock object.

## Parameters

- `UID`: The String UID of the clock object to obtain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/clock(foruid:))*