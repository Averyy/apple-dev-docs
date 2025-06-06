# SCPreferencesPathRemoveValue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Removes the data associated with the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathRemoveValue(_ prefs: SCPreferences, _ path: CFString) -> Bool
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.

## See Also

- [func SCPreferencesPathGetValue(SCPreferences, CFString) -> CFDictionary?](scpreferencespathgetvalue(_:_:).md)
  Returns the dictionary associated with the specified path.
- [func SCPreferencesPathGetLink(SCPreferences, CFString) -> CFString?](scpreferencespathgetlink(_:_:).md)
  Returns the link associated with the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathremovevalue(_:_:))*