# SCPreferencesAddValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Associates the specified value with the specified preference key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesAddValue(_ prefs: SCPreferences, _ key: CFString, _ value: CFPropertyList) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value was added; [`false`](https://developer.apple.com/documentation/Swift/false) if the key already exists or if an error occurred.

#### Discussion

To commit these changes to permanent storage, you must call [`SCPreferencesCommitChanges(_:)`](scpreferencescommitchanges(_:).md).

## Parameters

- `prefs`: The preferences session.
- `key`: The preference key.
- `value`: The value to associate with the preference key.

## See Also

- [func SCPreferencesGetValue(SCPreferences, CFString) -> CFPropertyList?](scpreferencesgetvalue(_:_:).md)
  Retrieves the value associated with the specified preference key.
- [func SCPreferencesSetValue(SCPreferences, CFString, CFPropertyList) -> Bool](scpreferencessetvalue(_:_:_:).md)
  Updates the data associated with the specified preference key with the specified value.
- [func SCPreferencesRemoveValue(SCPreferences, CFString) -> Bool](scpreferencesremovevalue(_:_:).md)
  Removes the data associated with the specified preference key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesaddvalue(_:_:_:))*