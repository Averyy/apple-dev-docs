# SCPreferencesSynchronize(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Synchronizes accessed preferences with committed changes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCPreferencesSynchronize(_ prefs: SCPreferences)
```

```c
void SCPreferencesSynchronize(SCPreferencesRef prefs);
```

#### Discussion

Any references to preference values returned by calls to [`SCPreferencesGetValue(_:_:)`](./scpreferencesgetvalue%28_,_%29.md) are no longer valid unless they were explicitly retained or copied. Any preference values that were updated (added, set, or removed), but not committed, are discarded.

## Parameters

- `prefs`: The preferences session.

## See Also

### Applying and Committing Changes
- [func SCPreferencesApplyChanges(SCPreferences) -> Bool](./scpreferencesapplychanges%28_%29.md)
  Requests that the currently stored configuration preferences be applied to the active configuration.
- [func SCPreferencesCommitChanges(SCPreferences) -> Bool](./scpreferencescommitchanges%28_%29.md)
  Commits changes made to the configuration preferences to persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessynchronize(_:))*