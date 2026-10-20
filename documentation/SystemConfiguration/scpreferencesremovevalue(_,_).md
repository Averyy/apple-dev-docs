# SCPreferencesRemoveValue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Removes the data associated with the specified preference key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesRemoveValue(_ prefs: SCPreferences, _ key: CFString) -> Bool
```

```c
Boolean SCPreferencesRemoveValue(SCPreferencesRef prefs, CFStringRef key);
```

#### Return Value

`TRUE` if the value was removed; `FALSE` if the key does not exist or if an error occurred.

## Parameters

- `prefs`: The preferences session.
- `key`: The preference key.

## See Also

### Adding, Getting, and Removing Values
- [func SCPreferencesAddValue(SCPreferences, CFString, CFPropertyList) -> Bool](./scpreferencesaddvalue%28_,_,_%29.md)
  Associates the specified value with the specified preference key.
- [func SCPreferencesGetValue(SCPreferences, CFString) -> CFPropertyList?](./scpreferencesgetvalue%28_,_%29.md)
  Retrieves the value associated with the specified preference key.
- [func SCPreferencesSetValue(SCPreferences, CFString, CFPropertyList) -> Bool](./scpreferencessetvalue%28_,_,_%29.md)
  Updates the data associated with the specified preference key with the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesremovevalue(_:_:))*