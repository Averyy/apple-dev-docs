# SCPreferencesSetValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Updates the data associated with the specified preference key with the specified value.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesSetValue(_ prefs: SCPreferences, _ key: CFString, _ value: CFPropertyList) -> Bool
```

```c
Boolean SCPreferencesSetValue(SCPreferencesRef prefs, CFStringRef key, CFPropertyListRef value);
```

## Return Value

`TRUE` if the value was set; `FALSE` if an error occurred.

## Discussion

This function adds or replaces the value associated with the specified key. To commit these changes to permanent storage you must call [`SCPreferencesCommitChanges(_:)`](./scpreferencescommitchanges%28_%29.md).

## Parameters

- `prefs`: The preferences session.
- `key`: The preference key.
- `value`: The value to associate with the preference key.

## See Also

### Adding, Getting, and Removing Values
- [func SCPreferencesAddValue(SCPreferences, CFString, CFPropertyList) -> Bool](./scpreferencesaddvalue%28_,_,_%29.md)
  Associates the specified value with the specified preference key.
- [func SCPreferencesGetValue(SCPreferences, CFString) -> CFPropertyList?](./scpreferencesgetvalue%28_,_%29.md)
  Retrieves the value associated with the specified preference key.
- [func SCPreferencesRemoveValue(SCPreferences, CFString) -> Bool](./scpreferencesremovevalue%28_,_%29.md)
  Removes the data associated with the specified preference key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetvalue(_:_:_:))*