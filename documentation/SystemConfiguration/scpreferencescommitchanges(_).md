# SCPreferencesCommitChanges(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Commits changes made to the configuration preferences to persistent storage.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesCommitChanges(_ prefs: SCPreferences) -> Bool
```

```c
Boolean SCPreferencesCommitChanges(SCPreferencesRef prefs);
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

#### Discussion

Implicit calls to the [`SCPreferencesLock(_:_:)`](./scpreferenceslock%28_,_%29.md) and [`SCPreferencesUnlock(_:)`](./scpreferencesunlock%28_%29.md) functions are made if exclusive access has not already been established.

> **Note**:  This function commits changes to persistent storage. To apply the changes to the running system, use the [`SCPreferencesApplyChanges(_:)`](./scpreferencesapplychanges%28_%29.md) function.

## Parameters

- `prefs`: The preferences session.

## See Also

### Applying and Committing Changes
- [func SCPreferencesApplyChanges(SCPreferences) -> Bool](./scpreferencesapplychanges%28_%29.md)
  Requests that the currently stored configuration preferences be applied to the active configuration.
- [func SCPreferencesSynchronize(SCPreferences)](./scpreferencessynchronize%28_%29.md)
  Synchronizes accessed preferences with committed changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescommitchanges(_:))*