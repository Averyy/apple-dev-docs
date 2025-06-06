# SCPreferencesPathCreateUniqueChild(_:_:)

**Framework**: System Configuration  
**Kind**: func

Creates a new path component rooted at the specified path in the dictionary hierarchy.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesPathCreateUniqueChild(_ prefs: SCPreferences, _ prefix: CFString) -> CFString?
```

#### Return Value

A string representing the new (unique) child path, or `NULL` if the specified path does not exist.

## Parameters

- `prefs`: The preferences session.
- `prefix`: The parent path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespathcreateuniquechild(_:_:))*