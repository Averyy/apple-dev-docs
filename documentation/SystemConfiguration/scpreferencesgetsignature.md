# SCPreferencesGetSignature(_:)

**Framework**: System Configuration  
**Kind**: func

Returns a value that can be used to determine if the saved configuration preferences have changed.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesGetSignature(_ prefs: SCPreferences) -> CFData?
```

#### Return Value

Data that reflects the signature of the configuration preferences at the time of the call to the [`SCPreferencesCreate(_:_:_:)`](scpreferencescreate(_:_:_:).md) function.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCPreferencesGetTypeID() -> CFTypeID](scpreferencesgettypeid().md)
  Returns the type identifier of all `SCPreferences` instances.
- [func SCPreferencesCopyKeyList(SCPreferences) -> CFArray?](scpreferencescopykeylist(_:).md)
  Returns the currently defined preference keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesgetsignature(_:))*