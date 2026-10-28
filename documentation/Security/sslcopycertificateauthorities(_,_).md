# SSLCopyCertificateAuthorities(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the current list of certification authorities.

**Availability**:
- macOS 10.5+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLCopyCertificateAuthorities(_ context: SSLContext, _ certificates: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

```c
OSStatus SSLCopyCertificateAuthorities(SSLContextRef context, CFArrayRef*certificates);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `certificates`: On return, a pointer to a value of type `CFArrayRef`. This array contains values of type `SecCertificateRef` representing the current set of certification authorities (specified with the [`SSLSetCertificateAuthorities(_:_:_:)`](./sslsetcertificateauthorities%28_,_,_%29.md) function). Returns a `NULL` array if [`SSLSetCertificateAuthorities(_:_:_:)`](./sslsetcertificateauthorities%28_,_,_%29.md) has not been called. You must call the `CFRelease` function to release this array when you are finished with it.

## See Also

### Related Documentation
- [func SSLCopyDistinguishedNames(SSLContext, UnsafeMutablePointer<CFArray?>) -> OSStatus](./sslcopydistinguishednames%28_,_%29.md)
  Retrieves the distinguished names of acceptable certification authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopycertificateauthorities(_:_:))*