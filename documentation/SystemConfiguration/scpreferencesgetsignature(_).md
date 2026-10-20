# SCPreferencesGetSignature(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns a value that can be used to determine if the saved configuration preferences have changed.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesGetSignature(_ prefs: SCPreferences) -> CFData?
```

```c
CFDataRefSCPreferencesGetSignature(SCPreferencesRef prefs);
```

#### Return Value

Data that reflects the signature of the configuration preferences at the time of the call to the [`SCPreferencesCreate(_:_:_:)`](./scpreferencescreate%28_,_,_%29.md) function.

## Parameters

- `prefs`: The preferences session.

## See Also

### Getting Information About a Preferences Session
- [func SCPreferencesGetTypeID() -> CFTypeID](./scpreferencesgettypeid%28%29.md)
  Returns the type identifier of all `SCPreferences` instances.
- [func SCPreferencesCopyKeyList(SCPreferences) -> CFArray?](./scpreferencescopykeylist%28_%29.md)
  Returns the currently defined preference keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesgetsignature(_:))*