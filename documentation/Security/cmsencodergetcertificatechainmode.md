# CMSEncoderGetCertificateChainMode(_:_:)

**Framework**: Security  
**Kind**: func

Obtains a constant that indicates which certificates are to be included in a signed CMS message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderGetCertificateChainMode(_ cmsEncoder: CMSEncoder, _ chainModeOut: UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `chainModeOut`: On return, a constant that indicates which certificate or certificates are to be included in the message. See  .

## See Also

- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodergetcertificatechainmode(_:_:))*