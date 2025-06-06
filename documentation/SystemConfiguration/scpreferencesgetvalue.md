# SCPreferencesGetValue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Retrieves the value associated with the specified preference key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesGetValue(_ prefs: SCPreferences, _ key: CFString) -> CFPropertyList?
```

#### Return Value

The value associated with the specified preference key (can be `NULL` if no value exists).

#### Discussion

To avoid inadvertantly reading stale data, first call [`SCPreferencesLock(_:_:)`](scpreferenceslock(_:_:).md) before calling this function.

## Parameters

- `prefs`: The preferences session.
- `key`: The preference key.

## See Also

- [func SCPreferencesAddValue(SCPreferences, CFString, CFPropertyList) -> Bool](scpreferencesaddvalue(_:_:_:).md)
  Associates the specified value with the specified preference key.
- [func SCPreferencesSetValue(SCPreferences, CFString, CFPropertyList) -> Bool](scpreferencessetvalue(_:_:_:).md)
  Updates the data associated with the specified preference key with the specified value.
- [func SCPreferencesRemoveValue(SCPreferences, CFString) -> Bool](scpreferencesremovevalue(_:_:).md)
  Removes the data associated with the specified preference key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesgetvalue(_:_:))*