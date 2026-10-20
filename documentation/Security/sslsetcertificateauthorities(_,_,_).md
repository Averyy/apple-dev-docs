# SSLSetCertificateAuthorities(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Adds one or more certificates to a server’s list of certification authorities (CAs) acceptable for client authentication.

**Availability**:
- macOS 10.5+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetCertificateAuthorities(_ context: SSLContext, _ certificateOrArray: CFTypeRef, _ replaceExisting: Bool) -> OSStatus
```

```c
OSStatus SSLSetCertificateAuthorities(SSLContextRef context, CFTypeRef certificateOrArray, Boolean replaceExisting);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md). Returns [`errSecParam`](./errsecparam.md) if this function is called for a session that is configured as a client, or when a session is active.

#### Discussion

Each successive call to this function with the `replaceExisting` parameter set to [`false`](../Swift/false.md) results in accumulation of additional certification authorities. To see the current set of certification authorities, call the [`SSLCopyCertificateAuthorities(_:_:)`](./sslcopycertificateauthorities%28_,_%29.md) function.

## Parameters

- `context`: An SSL session context reference.
- `certificateOrArray`: A value of type `SecCertificateRef`, or a value of type `CFArray` containing an array of `SecCertificateRef` values, representing one or more certificates to be added to the server’s list of acceptable certification authorities (CAs).
- `replaceExisting`: A Boolean value specifying whether to replace or append the current set of certification authorities. If this value is `true`, the specified certificates replace the existing list of acceptable CAs, if any. If `false`, the specified certificates are appended to the existing list of.

## See Also

### Related Documentation
- [func SSLCopyDistinguishedNames(SSLContext, UnsafeMutablePointer<CFArray?>) -> OSStatus](./sslcopydistinguishednames%28_,_%29.md)
  Retrieves the distinguished names of acceptable certification authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetcertificateauthorities(_:_:_:))*