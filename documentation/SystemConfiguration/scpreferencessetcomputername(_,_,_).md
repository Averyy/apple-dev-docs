# SCPreferencesSetComputerName(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Sets the computer name preference to the specified name.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesSetComputerName(_ prefs: SCPreferences, _ name: CFString?, _ nameEncoding: CFStringEncoding) -> Bool
```

```c
Boolean SCPreferencesSetComputerName(SCPreferencesRef prefs, CFStringRef name, CFStringEncoding nameEncoding);
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE`.

#### Discussion

To commit these changes to permanent storage you must call the [`SCPreferencesCommitChanges(_:)`](./scpreferencescommitchanges%28_%29.md) function. In addition, you must call the [`SCPreferencesApplyChanges(_:)`](./scpreferencesapplychanges%28_%29.md) function for the new name to become active.

## Parameters

- `prefs`: The preferences session.
- `name`: The computer name.
- `nameEncoding`: The encoding associated with the computer name.

## See Also

### Setting Configuration Information
- [func SCPreferencesSetLocalHostName(SCPreferences, CFString?) -> Bool](./scpreferencessetlocalhostname%28_,_%29.md)
  Sets the local host name to the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetcomputername(_:_:_:))*