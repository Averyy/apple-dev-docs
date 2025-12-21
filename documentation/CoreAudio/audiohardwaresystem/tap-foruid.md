# tap(forUID:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
func tap(forUID UID: String) throws -> AudioHardwareTap?
```

#### Return Value

The AudioHardwareTap that corresponds with the given UID, or nil if the UID does not correspond with any tap object.

## Parameters

- `UID`: The String UID of the tap object to obtain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/tap(foruid:))*