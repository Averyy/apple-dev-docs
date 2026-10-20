# SCPreferencesGetTypeID()

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the type identifier of all `SCPreferences` instances.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesGetTypeID() -> CFTypeID
```

```c
CFTypeID SCPreferencesGetTypeID();
```

## See Also

### Getting Information About a Preferences Session
- [func SCPreferencesCopyKeyList(SCPreferences) -> CFArray?](./scpreferencescopykeylist%28_%29.md)
  Returns the currently defined preference keys.
- [func SCPreferencesGetSignature(SCPreferences) -> CFData?](./scpreferencesgetsignature%28_%29.md)
  Returns a value that can be used to determine if the saved configuration preferences have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencesgettypeid())*