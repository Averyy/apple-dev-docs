# SCPreferencesLock(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Locks access to the configuration preferences.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesLock(_ prefs: SCPreferences, _ wait: Bool) -> Bool
```

```c
Boolean SCPreferencesLock(SCPreferencesRef prefs, Boolean wait);
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

#### Discussion

This function obtains exclusive access to the configuration preferences. Clients attempting to obtain exclusive access to the preferences either receive a [`kSCStatusPrefsBusy`](./kscstatusprefsbusy.md) error or they block, waiting for the lock to be released.

## Parameters

- `prefs`: The preferences session.
- `wait`: A Boolean value indicating whether the calling process should block, waiting for another process to complete its update operation and release its lock.

## See Also

### Managing Access to a Preferences Session
- [func SCPreferencesUnlock(SCPreferences) -> Bool](./scpreferencesunlock%28_%29.md)
  Releases exclusive access to the configuration preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferenceslock(_:_:))*