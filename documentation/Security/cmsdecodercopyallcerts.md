# CMSDecoderCopyAllCerts(_:_:)

**Framework**: Security  
**Kind**: func

Obtains an array of all of the certificates in a message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A CMS message can contain arbitrary sets of certificates other than or in addition to those indicating the identity of signers. You can use this function to retrieve such certificates from a message. If the message was signed, it contains signer certificates. You can use the [`CMSDecoderGetNumSigners(_:_:)`](cmsdecodergetnumsigners(_:_:).md) and [`CMSDecoderCopySignerCert(_:_:_:)`](cmsdecodercopysignercert(_:_:_:).md) functions to retrieve the certificates for a specific signer.

You cannot call this function until after you have called the [`CMSDecoderFinalizeMessage(_:)`](cmsdecoderfinalizemessage(_:).md) function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `certsOut`: On return, points to an array of   objects. Returns   if the message does not contain any certificates (the message was encrypted but not signed); this is not considered an error. You must use the   function to free this reference when you are finished using it.

## See Also

- [func CMSDecoderCopySignerCert(CMSDecoder, Int, UnsafeMutablePointer<SecCertificate?>) -> OSStatus](cmsdecodercopysignercert(_:_:_:).md)
  Obtains the certificate of the specified signer of a CMS message.
- [func CMSEncoderAddSupportingCerts(CMSEncoder, CFTypeRef) -> OSStatus](cmsencoderaddsupportingcerts(_:_:).md)
  Adds certificates to a message.
- [func CMSDecoderGetNumSigners(CMSDecoder, UnsafeMutablePointer<Int>) -> OSStatus](cmsdecodergetnumsigners(_:_:).md)
  Obtains the number of signers of a message.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](cmsdecoderfinalizemessage(_:).md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopyallcerts(_:_:))*