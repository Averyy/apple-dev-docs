# SCDynamicStoreCopyLocation(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the current location identifier.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyLocation(_ store: SCDynamicStore?) -> CFString?
```

#### Return Value

Returns the current location identifier, or `NULL` if no location identifier has been defined or if an error occurred. You must release the returned value.

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. Pass   to use a temporary session.

## See Also

- [func SCDynamicStoreCopyComputerName(SCDynamicStore?, UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](scdynamicstorecopycomputername(_:_:).md)
  Returns the current computer name.
- [func SCDynamicStoreCopyConsoleUser(SCDynamicStore?, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?) -> CFString?](scdynamicstorecopyconsoleuser(_:_:_:).md)
  Returns information about the user currently logged into the system.
- [func SCDynamicStoreCopyLocalHostName(SCDynamicStore?) -> CFString?](scdynamicstorecopylocalhostname(_:).md)
  Returns the current local host name.
- [func SCDynamicStoreCopyProxies(SCDynamicStore?) -> CFDictionary?](scdynamicstorecopyproxies(_:).md)
  Returns the key-value pairs that represent the current internet proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopylocation(_:))*