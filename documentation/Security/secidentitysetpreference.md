# SecIdentitySetPreference

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the preferred identity for the specified name and key use.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecIdentitySetPreference(SecIdentityRef identity, CFStringRef name, CSSM_KEYUSE keyUsage);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

Use [`SecIdentitySetPreferred(_:_:_:)`](./secidentitysetpreferred%28_,_,_%29.md) for new development instead.

## Parameters

- `identity`: A reference to the preferred identity.
- `name`: A string containing a URI, RFC822 email address, DNS host name, or other name that uniquely identifies a service requiring this identity.
- `keyUsage`: A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` if you don’t want to specify a particular key use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitysetpreference)*