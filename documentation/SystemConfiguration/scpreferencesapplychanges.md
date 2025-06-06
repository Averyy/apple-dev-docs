# SCPreferencesApplyChanges(_:)

**Framework**: System Configuration  
**Kind**: func

Requests that the currently stored configuration preferences be applied to the active configuration.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesApplyChanges(_ prefs: SCPreferences) -> Bool
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCPreferencesCommitChanges(SCPreferences) -> Bool](scpreferencescommitchanges(_:).md)
  Commits changes made to the configuration preferences to persistent storage.
- [func SCPreferencesSynchronize(SCPreferences)](scpreferencessynchronize(_:).md)
  Synchronizes accessed preferences with committed changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesapplychanges(_:))*