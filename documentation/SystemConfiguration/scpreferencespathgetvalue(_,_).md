# SCPreferencesPathGetValue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the dictionary associated with the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathGetValue(_ prefs: SCPreferences, _ path: CFString) -> CFDictionary?
```

```c
CFDictionaryRefSCPreferencesPathGetValue(SCPreferencesRef prefs, CFStringRef path);
```

#### Return Value

The dictionary associated with the specified path, or `NULL` if the path does not exist.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.

## See Also

### Getting or Removing Information Associated with a Path
- [func SCPreferencesPathGetLink(SCPreferences, CFString) -> CFString?](./scpreferencespathgetlink%28_,_%29.md)
  Returns the link associated with the specified path.
- [func SCPreferencesPathRemoveValue(SCPreferences, CFString) -> Bool](./scpreferencespathremovevalue%28_,_%29.md)
  Removes the data associated with the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathgetvalue(_:_:))*