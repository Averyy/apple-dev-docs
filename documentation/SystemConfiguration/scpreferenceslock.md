# SCPreferencesLock(_:_:)

**Framework**: System Configuration  
**Kind**: func

Locks access to the configuration preferences.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesLock(_ prefs: SCPreferences, _ wait: Bool) -> Bool
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

#### Discussion

This function obtains exclusive access to the configuration preferences. Clients attempting to obtain exclusive access to the preferences either receive a [`kSCStatusPrefsBusy`](kscstatusprefsbusy.md) error or they block, waiting for the lock to be released.

## Parameters

- `prefs`: The preferences session.
- `wait`: A Boolean value indicating whether the calling process should block, waiting for another process to complete its update operation and release its lock.

## See Also

- [func SCPreferencesUnlock(SCPreferences) -> Bool](scpreferencesunlock(_:).md)
  Releases exclusive access to the configuration preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferenceslock(_:_:))*