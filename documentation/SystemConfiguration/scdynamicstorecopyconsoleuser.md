# SCDynamicStoreCopyConsoleUser(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Returns information about the user currently logged into the system.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore?, _ uid: UnsafeMutablePointer<uid_t>?, _ gid: UnsafeMutablePointer<gid_t>?) -> CFString?
```

#### Return Value

Returns the name, user ID, and group ID of the user currently logged into the system, or `NULL` if no user is logged in or if an error occurred. You must release the returned values.

#### Discussion

Note that this function only provides information about the primary console. It does not provide any details about console sessions that have fast user switched out or about other consoles.

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. Pass   to use a temporary session.
- `uid`: A pointer to memory that, on output, is filled with the user ID of the currently logged-in user. If  , this value is not returned.
- `gid`: A pointer to memory that, on output, is filled with the group ID of the currently logged-in user. If  , this value is not returned.

## See Also

- [func SCDynamicStoreCopyComputerName(SCDynamicStore?, UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](scdynamicstorecopycomputername(_:_:).md)
  Returns the current computer name.
- [func SCDynamicStoreCopyLocalHostName(SCDynamicStore?) -> CFString?](scdynamicstorecopylocalhostname(_:).md)
  Returns the current local host name.
- [func SCDynamicStoreCopyLocation(SCDynamicStore?) -> CFString?](scdynamicstorecopylocation(_:).md)
  Returns the current location identifier.
- [func SCDynamicStoreCopyProxies(SCDynamicStore?) -> CFDictionary?](scdynamicstorecopyproxies(_:).md)
  Returns the key-value pairs that represent the current internet proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopyconsoleuser(_:_:_:))*