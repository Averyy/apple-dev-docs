# device(forUID:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func device(forUID UID: String) throws -> AudioHardwareDevice?
```

#### Return Value

The AudioHardwareDevice that corresponds with the given UID, or nil if the UID does not correspond with any device object.

## Parameters

- `UID`: The String UID of the device object to obtain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/device(foruid:))*