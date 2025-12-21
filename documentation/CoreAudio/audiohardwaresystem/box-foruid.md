# box(forUID:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func box(forUID UID: String) throws -> AudioHardwareBox?
```

#### Return Value

The AudioHardwareBox that corresponds with the given UID, or nil if the UID does not correspond with any box object.

## Parameters

- `UID`: The String UID of the box object to obtain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/box(foruid:))*