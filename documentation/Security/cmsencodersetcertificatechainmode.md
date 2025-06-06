# CMSEncoderSetCertificateChainMode(_:_:)

**Framework**: Security  
**Kind**: func

Specifies which certificates to include in a signed CMS message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderSetCertificateChainMode(_ cmsEncoder: CMSEncoder, _ chainMode: CMSCertificateChainMode) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function is used only for signed messages and is optional. If you don’t call this function, the default, `kCMSCertificateChain`, is used. In this case the message includes the signer certificate plus all certificates needed to verify the signer certificate, up to but not including the root  certificate.

If you do call this function, you must call it before the first call to the `CMSEncoderUpdateContent` function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `chainMode`: A constant that indicates which certificate or certificates to include in the message. See  .

## See Also

- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](cmsencoderupdatecontent(_:_:_:).md)
  Feeds content bytes into the encoder.
- [func CMSEncoderGetCertificateChainMode(CMSEncoder, UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus](cmsencodergetcertificatechainmode(_:_:).md)
  Obtains a constant that indicates which certificates are to be included in a signed CMS message.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodersetcertificatechainmode(_:_:))*