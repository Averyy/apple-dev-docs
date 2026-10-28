# SCPreferencesPathSetValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Associates the specified dictionary with the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathSetValue(_ prefs: SCPreferences, _ path: CFString, _ value: CFDictionary) -> Bool
```

```c
Boolean SCPreferencesPathSetValue(SCPreferencesRef prefs, CFStringRef path, CFDictionaryRef value);
```

## Return Value

`TRUE` if successful; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.
- `value`: The dictionary of data to be stored at the path.

## See Also

### Associating Information with a Path
- [func SCPreferencesPathSetLink(SCPreferences, CFString, CFString) -> Bool](./scpreferencespathsetlink%28_,_,_%29.md)
  Associates a link to a second dictionary at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathsetvalue(_:_:_:))*