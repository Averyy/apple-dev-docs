# SSLCopyDistinguishedNames(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the distinguished names of acceptable certification authorities.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func SSLCopyDistinguishedNames(_ context: SSLContext, _ names: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

The list of distinguished names is provided by the server if the context reference represents a client; if the context reference represents a server, the list of distinguished names is specified with the [`SSLSetCertificateAuthorities(_:_:_:)`](sslsetcertificateauthorities(_:_:_:).md) function.

The array retrieved by this function is suitable for use in finding a client identity (that is, a certificate and associated private key) that matches a server’s requirements.

## Parameters

- `context`: An SSL session context reference.
- `names`: On return, an array of   objects, each representing one DER-encoded relative distinguished name of an acceptable certification authority. You must call the   function to release this array when you are finished with it.

## See Also

- [func SSLSetCertificateAuthorities(SSLContext, CFTypeRef, Bool) -> OSStatus](sslsetcertificateauthorities(_:_:_:).md)
  Adds one or more certificates to a server’s list of certification authorities (CAs) acceptable for client authentication.
- [func SSLCopyCertificateAuthorities(SSLContext, UnsafeMutablePointer<CFArray?>) -> OSStatus](sslcopycertificateauthorities(_:_:).md)
  Retrieves the current list of certification authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopydistinguishednames(_:_:))*