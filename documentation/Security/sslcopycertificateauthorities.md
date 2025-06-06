# SSLCopyCertificateAuthorities(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the current list of certification authorities.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SSLCopyCertificateAuthorities(_ context: SSLContext, _ certificates: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `certificates`: On return, a pointer to a value of type  . This array contains values of type   representing the current set of certification authorities (specified with the   function). Returns a   array if   has not been called. You must call the   function to release this array when you are finished with it.

## See Also

- [func SSLCopyDistinguishedNames(SSLContext, UnsafeMutablePointer<CFArray?>) -> OSStatus](sslcopydistinguishednames(_:_:).md)
  Retrieves the distinguished names of acceptable certification authorities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopycertificateauthorities(_:_:))*