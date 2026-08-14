# SCPreferencesCreateWithAuthorization(_:_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Initiates access to the per-system set of configuration preferences with the specified authorization.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator?, _ name: CFString, _ prefsID: CFString?, _ authorization: AuthorizationRef?) -> SCPreferences?
```

#### Return Value

A reference to the new preferences session. You must release the returned value.

## Parameters

- `allocator`: The allocator to use to allocate memory for this preferences session. If the value is not a valid `CFAllocator`, the behavior is undefined. Pass `NULL` or [`kCFAllocatorDefault`](https://developer.apple.com/documentation/corefoundation/kcfallocatordefault) to use the current default `CFAllocator`.
- `name`: The name of the calling process.
- `prefsID`: The name of the group of preferences to be accessed or updated. A name that starts with a leading “/” character specifies the absolute path to the file containing the preferences to be accessed. A name that does not start with a leading “/” character specifies a file relative to the default system preferences directory. To access the default system preferences, pass in `NULL`.
- `authorization`: An authorization reference that is used to authorize any access to the enhanced privileges needed to manage the preferences session.

## See Also

- [func SCPreferencesCreate(CFAllocator?, CFString, CFString?) -> SCPreferences?](scpreferencescreate(_:_:_:).md)
  Initiates access to the per-system set of configuration preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescreatewithauthorization(_:_:_:_:))*