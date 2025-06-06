# SCPreferencesSynchronize(_:)

**Framework**: System Configuration  
**Kind**: func

Synchronizes accessed preferences with committed changes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCPreferencesSynchronize(_ prefs: SCPreferences)
```

#### Discussion

Any references to preference values returned by calls to [`SCPreferencesGetValue(_:_:)`](scpreferencesgetvalue(_:_:).md) are no longer valid unless they were explicitly retained or copied. Any preference values that were updated (added, set, or removed), but not committed, are discarded.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCPreferencesApplyChanges(SCPreferences) -> Bool](scpreferencesapplychanges(_:).md)
  Requests that the currently stored configuration preferences be applied to the active configuration.
- [func SCPreferencesCommitChanges(SCPreferences) -> Bool](scpreferencescommitchanges(_:).md)
  Commits changes made to the configuration preferences to persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessynchronize(_:))*