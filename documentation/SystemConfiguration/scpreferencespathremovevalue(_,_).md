# SCPreferencesPathRemoveValue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Removes the data associated with the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathRemoveValue(_ prefs: SCPreferences, _ path: CFString) -> Bool
```

```c
Boolean SCPreferencesPathRemoveValue(SCPreferencesRef prefs, CFStringRef path);
```

## Return Value

`TRUE` if successful; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.

## See Also

### Getting or Removing Information Associated with a Path
- [func SCPreferencesPathGetValue(SCPreferences, CFString) -> CFDictionary?](./scpreferencespathgetvalue%28_,_%29.md)
  Returns the dictionary associated with the specified path.
- [func SCPreferencesPathGetLink(SCPreferences, CFString) -> CFString?](./scpreferencespathgetlink%28_,_%29.md)
  Returns the link associated with the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathremovevalue(_:_:))*