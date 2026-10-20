# SCPreferencesSetLocalHostName(_:_:)

**Framework**: System Configuration  
**Kind**: func

Sets the local host name to the specified name.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SCPreferencesSetLocalHostName(_ prefs: SCPreferences, _ name: CFString?) -> Bool
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE`.

#### Discussion

To commit these changes to permanent storage you must call the [`SCPreferencesCommitChanges(_:)`](scpreferencescommitchanges(_:).md) function. In addition, you must call the [`SCPreferencesApplyChanges(_:)`](scpreferencesapplychanges(_:).md) function for the new name to become active.

## Parameters

- `prefs`: The preferences session.
- `name`: The local host name. This string must conform to the naming conventions of a DNS host name as specified in RFC 1034 (section 3.5).

## See Also

- [func SCPreferencesSetComputerName(SCPreferences, CFString?, CFStringEncoding) -> Bool](scpreferencessetcomputername(_:_:_:).md)
  Sets the computer name preference to the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetlocalhostname(_:_:))*