# CMSDecoderCopySignerCert(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the certificate of the specified signer of a CMS message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signerCertOut: UnsafeMutablePointer<SecCertificate?>) -> OSStatus
```

```c
OSStatus CMSDecoderCopySignerCert(CMSDecoderRef cmsDecoder, size_t signerIndex, SecCertificateRef*signerCertOut);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). Returns [`errSecParam`](./errsecparam.md) if the CMS message was not signed or if `signerIndex` is greater than the number of signers of the message minus one (signerIndex > (numSigners – 1)).

#### Discussion

You cannot call this function until after you have called the [`CMSDecoderFinalizeMessage(_:)`](./cmsdecoderfinalizemessage%28_%29.md) function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `signerIndex`: A number indicating which signer’s email address to return. Signer index numbers start with 0. Use the [`CMSDecoderGetNumSigners(_:_:)`](./cmsdecodergetnumsigners%28_,_%29.md) function to determine the total number of signers for a message.
- `signerCertOut`: On return, points to the certificate of the specified signer.

## See Also

### Related Documentation
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignercert(_:_:_:))*