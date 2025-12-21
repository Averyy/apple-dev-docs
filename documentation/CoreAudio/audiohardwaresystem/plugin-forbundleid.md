# plugin(forBundleID:)

**Framework**: Core Audio  
**Kind**: method

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func plugin(forBundleID ID: String) throws -> AudioHardwarePlugin?
```

#### Return Value

The AudioHardwarePlugin that corresponds with the given bundle ID, or nil if the ID does not correspond with any plugin object.

## Parameters

- `ID`: The String bundle ID of the plugin object to obtain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/plugin(forbundleid:))*