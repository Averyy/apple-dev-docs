# SecIdentityCopyPreference

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the preferred identity for the specified name and key use.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecIdentityCopyPreference(CFStringRef name, CSSM_KEYUSE keyUsage, CFArrayRef validIssuers, SecIdentityRef*identity);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

If a preferred identity has not been set for the specified name, the returned identity reference is `NULL`. You should then typically perform a search for possible identities, using [`SecIdentitySearchCreate`](./secidentitysearchcreate.md) and [`SecIdentitySearchCopyNext`](./secidentitysearchcopynext.md), allowing the user to choose from a list if more than one is found.

##### Special Considerations

Use [`SecIdentityCopyPreferred(_:_:_:)`](./secidentitycopypreferred%28_,_,_%29.md) for new development instead.

## Parameters

- `name`: A string containing a URI, RFC822 email address, DNS hostname, or other name that uniquely identifies the service requiring an identity.
- `keyUsage`: A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` if you don’t want to specify a particular key use.
- `validIssuers`: An array of `CFDataRef` instances whose contents are the subject names of allowable issuers, as returned by a call to `SSLCopyDistinguishedNames` (`Security.framework/SecureTransport.h`). Pass `NULL` if you don’t want to limit the search to specific issuers.
- `identity`: On return, a reference to the preferred identity, or `NULL` if none was found. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycopypreference)*