# SCPreferencesAddValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Associates the specified value with the specified preference key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesAddValue(_ prefs: SCPreferences, _ key: CFString, _ value: CFPropertyList) -> Bool
```

```c
Boolean SCPreferencesAddValue(SCPreferencesRef prefs, CFStringRef key, CFPropertyListRef value);
```

## Return Value

[`true`](../Swift/true.md) if the value was added; [`false`](../Swift/false.md) if the key already exists or if an error occurred.

## Discussion

To commit these changes to permanent storage, you must call [`SCPreferencesCommitChanges(_:)`](./scpreferencescommitchanges%28_%29.md).

## Parameters

- `prefs`: The preferences session.
- `key`: The preference key.
- `value`: The value to associate with the preference key.

## See Also

### Adding, Getting, and Removing Values
- [func SCPreferencesGetValue(SCPreferences, CFString) -> CFPropertyList?](./scpreferencesgetvalue%28_,_%29.md)
  Retrieves the value associated with the specified preference key.
- [func SCPreferencesSetValue(SCPreferences, CFString, CFPropertyList) -> Bool](./scpreferencessetvalue%28_,_,_%29.md)
  Updates the data associated with the specified preference key with the specified value.
- [func SCPreferencesRemoveValue(SCPreferences, CFString) -> Bool](./scpreferencesremovevalue%28_,_%29.md)
  Removes the data associated with the specified preference key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesaddvalue(_:_:_:))*