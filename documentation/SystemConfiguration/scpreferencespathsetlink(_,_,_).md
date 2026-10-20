# SCPreferencesPathSetLink(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Associates a link to a second dictionary at the specified path.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathSetLink(_ prefs: SCPreferences, _ path: CFString, _ link: CFString) -> Bool
```

```c
Boolean SCPreferencesPathSetLink(SCPreferencesRef prefs, CFStringRef path, CFStringRef link);
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE`.

## Parameters

- `prefs`: The preferences session.
- `path`: The path.
- `link`: The link to be stored at the path.

## See Also

### Associating Information with a Path
- [func SCPreferencesPathSetValue(SCPreferences, CFString, CFDictionary) -> Bool](./scpreferencespathsetvalue%28_,_,_%29.md)
  Associates the specified dictionary with the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathsetlink(_:_:_:))*