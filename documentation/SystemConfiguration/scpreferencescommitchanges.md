# SCPreferencesCommitChanges(_:)

**Framework**: Systemconfiguration  
**Kind**: func

Commits changes made to the configuration preferences to persistent storage.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesCommitChanges(_ prefs: SCPreferences) -> Bool
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

#### Discussion

Implicit calls to the [`SCPreferencesLock(_:_:)`](scpreferenceslock(_:_:).md) and [`SCPreferencesUnlock(_:)`](scpreferencesunlock(_:).md) functions are made if exclusive access has not already been established.

> **Note**:  This function commits changes to persistent storage. To apply the changes to the running system, use the [`SCPreferencesApplyChanges(_:)`](scpreferencesapplychanges(_:).md) function.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCPreferencesApplyChanges(SCPreferences) -> Bool](scpreferencesapplychanges(_:).md)
  Requests that the currently stored configuration preferences be applied to the active configuration.
- [func SCPreferencesSynchronize(SCPreferences)](scpreferencessynchronize(_:).md)
  Synchronizes accessed preferences with committed changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescommitchanges(_:))*