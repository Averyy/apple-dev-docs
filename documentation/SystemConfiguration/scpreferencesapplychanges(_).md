# SCPreferencesApplyChanges(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Requests that the currently stored configuration preferences be applied to the active configuration.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesApplyChanges(_ prefs: SCPreferences) -> Bool
```

```c
Boolean SCPreferencesApplyChanges(SCPreferencesRef prefs);
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

## Parameters

- `prefs`: The preferences session.

## See Also

### Applying and Committing Changes
- [func SCPreferencesCommitChanges(SCPreferences) -> Bool](./scpreferencescommitchanges%28_%29.md)
  Commits changes made to the configuration preferences to persistent storage.
- [func SCPreferencesSynchronize(SCPreferences)](./scpreferencessynchronize%28_%29.md)
  Synchronizes accessed preferences with committed changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesapplychanges(_:))*