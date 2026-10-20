# SCPreferencesPathGetLink(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the link associated with the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathGetLink(_ prefs: SCPreferences, _ path: CFString) -> CFString?
```

```c
CFStringRefSCPreferencesPathGetLink(SCPreferencesRef prefs, CFStringRef path);
```

#### Return Value

The link associated with the specified path, or `NULL` if the path is not a link or does not exist.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.

## See Also

### Getting or Removing Information Associated with a Path
- [func SCPreferencesPathGetValue(SCPreferences, CFString) -> CFDictionary?](./scpreferencespathgetvalue%28_,_%29.md)
  Returns the dictionary associated with the specified path.
- [func SCPreferencesPathRemoveValue(SCPreferences, CFString) -> Bool](./scpreferencespathremovevalue%28_,_%29.md)
  Removes the data associated with the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathgetlink(_:_:))*