# SCPreferencesUnlock(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Releases exclusive access to the configuration preferences.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesUnlock(_ prefs: SCPreferences) -> Bool
```

```c
Boolean SCPreferencesUnlock(SCPreferencesRef prefs);
```

## Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

## Discussion

After exclusive access has been released, other clients can establish exclusive access to the preferences.

## Parameters

- `prefs`: The preferences session.

## See Also

### Managing Access to a Preferences Session
- [func SCPreferencesLock(SCPreferences, Bool) -> Bool](./scpreferenceslock%28_,_%29.md)
  Locks access to the configuration preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesunlock(_:))*