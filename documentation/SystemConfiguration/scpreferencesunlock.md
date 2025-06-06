# SCPreferencesUnlock(_:)

**Framework**: System Configuration  
**Kind**: func

Releases exclusive access to the configuration preferences.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesUnlock(_ prefs: SCPreferences) -> Bool
```

#### Return Value

`TRUE` if the lock was obtained; `FALSE` if an error occurred.

#### Discussion

After exclusive access has been released, other clients can establish exclusive access to the preferences.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCPreferencesLock(SCPreferences, Bool) -> Bool](scpreferenceslock(_:_:).md)
  Locks access to the configuration preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesunlock(_:))*