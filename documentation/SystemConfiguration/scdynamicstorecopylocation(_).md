# SCDynamicStoreCopyLocation(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the current location identifier.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyLocation(_ store: SCDynamicStore?) -> CFString?
```

```c
CFStringRefSCDynamicStoreCopyLocation(SCDynamicStoreRef store);
```

## Return Value

Returns the current location identifier, or `NULL` if no location identifier has been defined or if an error occurred. You must release the returned value.

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. Pass `NULL` to use a temporary session.

## See Also

### Group
- [func SCDynamicStoreCopyComputerName(SCDynamicStore?, UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](./scdynamicstorecopycomputername%28_,_%29.md)
  Returns the current computer name.
- [func SCDynamicStoreCopyConsoleUser(SCDynamicStore?, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?) -> CFString?](./scdynamicstorecopyconsoleuser%28_,_,_%29.md)
  Returns information about the user currently logged into the system.
- [func SCDynamicStoreCopyLocalHostName(SCDynamicStore?) -> CFString?](./scdynamicstorecopylocalhostname%28_%29.md)
  Returns the current local host name.
- [func SCDynamicStoreCopyProxies(SCDynamicStore?) -> CFDictionary?](./scdynamicstorecopyproxies%28_%29.md)
  Returns the key-value pairs that represent the current internet proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopylocation(_:))*