# SCPreferencesCreate(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Initiates access to the per-system set of configuration preferences.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCPreferencesCreate(_ allocator: CFAllocator?, _ name: CFString, _ prefsID: CFString?) -> SCPreferences?
```

#### Return Value

A reference to the new preferences session. You must release the returned value.

## Parameters

- `allocator`: The allocator to use to allocate memory for this preferences session. If the value is not a valid  , the behavior is undefined. Pass   or   to use the current default  .
- `name`: The name of the calling process.
- `prefsID`: To access the default system preferences, pass in  .

## See Also

- [func SCPreferencesCreateWithAuthorization(CFAllocator?, CFString, CFString?, AuthorizationRef?) -> SCPreferences?](scpreferencescreatewithauthorization(_:_:_:_:).md)
  Initiates access to the per-system set of configuration preferences with the specified authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescreate(_:_:_:))*