# SCPreferencesPathSetValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Associates the specified dictionary with the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathSetValue(_ prefs: SCPreferences, _ path: CFString, _ value: CFDictionary) -> Bool
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.
- `value`: The dictionary of data to be stored at the path.

## See Also

- [func SCPreferencesPathSetLink(SCPreferences, CFString, CFString) -> Bool](scpreferencespathsetlink(_:_:_:).md)
  Associates a link to a second dictionary at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathsetvalue(_:_:_:))*