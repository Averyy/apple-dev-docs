# SCPreferencesCopyKeyList(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the currently defined preference keys.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesCopyKeyList(_ prefs: SCPreferences) -> CFArray?
```

#### Return Value

An array of currently defined preference keys. You must release the returned value.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCPreferencesGetTypeID() -> CFTypeID](scpreferencesgettypeid().md)
  Returns the type identifier of all `SCPreferences` instances.
- [func SCPreferencesGetSignature(SCPreferences) -> CFData?](scpreferencesgetsignature(_:).md)
  Returns a value that can be used to determine if the saved configuration preferences have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescopykeylist(_:))*