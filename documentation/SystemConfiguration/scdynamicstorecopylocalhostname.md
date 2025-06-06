# SCDynamicStoreCopyLocalHostName(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the current local host name.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyLocalHostName(_ store: SCDynamicStore?) -> CFString?
```

#### Return Value

Returns the current local host name, or `NULL` if the name has not been set or if an error occurred. You must release the return value.

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. Pass   to use a temporary session.

## See Also

- [func SCDynamicStoreCopyComputerName(SCDynamicStore?, UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](scdynamicstorecopycomputername(_:_:).md)
  Returns the current computer name.
- [func SCDynamicStoreCopyConsoleUser(SCDynamicStore?, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?) -> CFString?](scdynamicstorecopyconsoleuser(_:_:_:).md)
  Returns information about the user currently logged into the system.
- [func SCDynamicStoreCopyLocation(SCDynamicStore?) -> CFString?](scdynamicstorecopylocation(_:).md)
  Returns the current location identifier.
- [func SCDynamicStoreCopyProxies(SCDynamicStore?) -> CFDictionary?](scdynamicstorecopyproxies(_:).md)
  Returns the key-value pairs that represent the current internet proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopylocalhostname(_:))*