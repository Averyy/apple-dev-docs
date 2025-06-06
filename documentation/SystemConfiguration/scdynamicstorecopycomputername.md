# SCDynamicStoreCopyComputerName(_:_:)

**Framework**: System Configuration  
**Kind**: func

Returns the current computer name.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore?, _ nameEncoding: UnsafeMutablePointer<CFStringEncoding>?) -> CFString?
```

#### Return Value

The current computer name, or `NULL` if the name has not been set or if an error occurred. You must release the return value.

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. Pass   to use a temporary session.
- `nameEncoding`: A pointer to memory that, on output, is filled with the encoding associated with the computer or host name, if it is non- .

## See Also

- [func SCDynamicStoreCopyConsoleUser(SCDynamicStore?, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?) -> CFString?](scdynamicstorecopyconsoleuser(_:_:_:).md)
  Returns information about the user currently logged into the system.
- [func SCDynamicStoreCopyLocalHostName(SCDynamicStore?) -> CFString?](scdynamicstorecopylocalhostname(_:).md)
  Returns the current local host name.
- [func SCDynamicStoreCopyLocation(SCDynamicStore?) -> CFString?](scdynamicstorecopylocation(_:).md)
  Returns the current location identifier.
- [func SCDynamicStoreCopyProxies(SCDynamicStore?) -> CFDictionary?](scdynamicstorecopyproxies(_:).md)
  Returns the key-value pairs that represent the current internet proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopycomputername(_:_:))*