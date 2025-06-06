# SCDynamicStoreCopyProxies(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the key-value pairs that represent the current internet proxy settings.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyProxies(_ store: SCDynamicStore?) -> CFDictionary?
```

#### Return Value

A dictionary of key-value pairs that represent the current internet proxy settings, or `NULL` if no proxy settings have been defined or if an error occurred. You must release the returned value.

#### Discussion

The returned proxy settings dictionary can include the following key-value pairs:

| Key | Type | Description |
| --- | --- | --- |
| `kSCPropNetProxiesExceptionsList` | A `CFArray` of `CFString` objects | Host name patterns that should bypass the proxy |
| `kSCPropNetProxiesHTTPEnable` | A `CFNumber` with the value `0` or `1` | Enables or disables the use of an HTTP proxy |
| `kSCPropNetProxiesHTTPProxy` | `CFString` | The proxy host |
| `kSCPropNetProxiesHTTPPort` | `CFNumber` | The proxy port number |
| `kSCPropNetProxiesHTTPSEnable` | A `CFNumber` with the value `0` or `1` | Enables or disables the use of an HTTPS proxy |
| `kSCPropNetProxiesHTTPSProxy` | `CFString` | The proxy host |
| `kSCPropNetProxiesHTTPSPort` | `CFNumber` | The proxy port number |
| `kSCPropNetProxiesFTPEnable` | A `CFNumber` with the value `0` or `1` | Enables or disables the use of an FTP proxy |
| `kSCPropNetProxiesFTPProxy` | `CFString` | The proxy host |
| `kSCPropNetProxiesFTPPort` | `CFNumber` | The proxy port number |
| `kSCPropNetProxiesFTPPassive` | A `CFNumber` with the value `0` or `1` | Enables or disables passive mode operation for use behind connection filtering firewalls |

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. Pass   to use a temporary session.

## See Also

- [func SCDynamicStoreCopyComputerName(SCDynamicStore?, UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](scdynamicstorecopycomputername(_:_:).md)
  Returns the current computer name.
- [func SCDynamicStoreCopyConsoleUser(SCDynamicStore?, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?) -> CFString?](scdynamicstorecopyconsoleuser(_:_:_:).md)
  Returns information about the user currently logged into the system.
- [func SCDynamicStoreCopyLocalHostName(SCDynamicStore?) -> CFString?](scdynamicstorecopylocalhostname(_:).md)
  Returns the current local host name.
- [func SCDynamicStoreCopyLocation(SCDynamicStore?) -> CFString?](scdynamicstorecopylocation(_:).md)
  Returns the current location identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopyproxies(_:))*