# SCPreferencesCopyKeyList(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the currently defined preference keys.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesCopyKeyList(_ prefs: SCPreferences) -> CFArray?
```

```c
CFArrayRefSCPreferencesCopyKeyList(SCPreferencesRef prefs);
```

## Return Value

An array of currently defined preference keys. You must release the returned value.

## Parameters

- `prefs`: The preferences session.

## See Also

### Getting Information About a Preferences Session
- [func SCPreferencesGetTypeID() -> CFTypeID](./scpreferencesgettypeid%28%29.md)
  Returns the type identifier of all `SCPreferences` instances.
- [func SCPreferencesGetSignature(SCPreferences) -> CFData?](./scpreferencesgetsignature%28_%29.md)
  Returns a value that can be used to determine if the saved configuration preferences have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescopykeylist(_:))*