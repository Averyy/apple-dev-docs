# SecKeyGetCredentials

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns an access credential for a key.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecKeyGetCredentials(SecKeyRef keyRef, CSSM_ACL_AUTHORIZATION_TAG operation, SecCredentialType credentialType, const CSSM_ACCESS_CREDENTIALS **outCredentials);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

An access credential is required as an input to a number of CSSM functions.

## Parameters

- `keyRef`: The key for which you want an access credential.
- `operation`: The type of operation to be performed with this key. Possible values are listed under “Authorization tag types” in `Security.framework/cssmtype.h`.
- `credentialType`: The type of credential requested. See [`SecCredentialType`](./seccredentialtype.md) for possible values.
- `outCredentials`: On return, points to an access credential for the specified key. This pointer remains valid until the key reference is released. Do not attempt to modify or free this data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygetcredentials)*