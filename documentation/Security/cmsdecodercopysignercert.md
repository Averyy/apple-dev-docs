# CMSDecoderCopySignerCert(_:_:_:)

**Framework**: Security  
**Kind**: func

Obtains the certificate of the specified signer of a CMS message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signerCertOut: UnsafeMutablePointer<SecCertificate?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Returns [`errSecParam`](errsecparam.md) if the CMS message was not signed or if `signerIndex` is greater than the number of signers of the message minus one (signerIndex > (numSigners – 1)).

#### Discussion

You cannot call this function until after you have called the [`CMSDecoderFinalizeMessage(_:)`](cmsdecoderfinalizemessage(_:).md) function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `signerIndex`: A number indicating which signer’s email address to return. Signer index numbers start with 0. Use the   function to determine the total number of signers for a message.
- `signerCertOut`: On return, points to the certificate of the specified signer.

## See Also

- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](cmsdecoderfinalizemessage(_:).md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignercert(_:_:_:))*