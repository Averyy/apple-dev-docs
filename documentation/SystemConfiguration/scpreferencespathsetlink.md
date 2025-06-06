# SCPreferencesPathSetLink(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Associates a link to a second dictionary at the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathSetLink(_ prefs: SCPreferences, _ path: CFString, _ link: CFString) -> Bool
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.
- `link`: The link to be stored at the path.

## See Also

- [func SCPreferencesPathSetValue(SCPreferences, CFString, CFDictionary) -> Bool](scpreferencespathsetvalue(_:_:_:).md)
  Associates the specified dictionary with the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathsetlink(_:_:_:))*