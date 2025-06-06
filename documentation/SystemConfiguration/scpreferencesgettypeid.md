# SCPreferencesGetTypeID()

**Framework**: System Configuration  
**Kind**: func

Returns the type identifier of all `SCPreferences` instances.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesGetTypeID() -> CFTypeID
```

## See Also

- [func SCPreferencesCopyKeyList(SCPreferences) -> CFArray?](scpreferencescopykeylist(_:).md)
  Returns the currently defined preference keys.
- [func SCPreferencesGetSignature(SCPreferences) -> CFData?](scpreferencesgetsignature(_:).md)
  Returns a value that can be used to determine if the saved configuration preferences have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesgettypeid())*