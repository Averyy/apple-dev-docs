# CMSDecoderCopyAllCerts(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains an array of all of the certificates in a message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

```c
OSStatus CMSDecoderCopyAllCerts(CMSDecoderRef cmsDecoder, CFArrayRef*certsOut);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

A CMS message can contain arbitrary sets of certificates other than or in addition to those indicating the identity of signers. You can use this function to retrieve such certificates from a message. If the message was signed, it contains signer certificates. You can use the [`CMSDecoderGetNumSigners(_:_:)`](./cmsdecodergetnumsigners%28_,_%29.md) and [`CMSDecoderCopySignerCert(_:_:_:)`](./cmsdecodercopysignercert%28_,_,_%29.md) functions to retrieve the certificates for a specific signer.

You cannot call this function until after you have called the [`CMSDecoderFinalizeMessage(_:)`](./cmsdecoderfinalizemessage%28_%29.md) function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `certsOut`: On return, points to an array of `SecCertificateRef` objects. Returns `NULL` if the message does not contain any certificates (the message was encrypted but not signed); this is not considered an error. You must use the `CFRelease` function to free this reference when you are finished using it.

## See Also

### Related Documentation
- [func CMSDecoderCopySignerCert(CMSDecoder, Int, UnsafeMutablePointer<SecCertificate?>) -> OSStatus](./cmsdecodercopysignercert%28_,_,_%29.md)
  Obtains the certificate of the specified signer of a CMS message.
- [func CMSEncoderAddSupportingCerts(CMSEncoder, CFTypeRef) -> OSStatus](./cmsencoderaddsupportingcerts%28_,_%29.md)
  Adds certificates to a message.
- [func CMSDecoderGetNumSigners(CMSDecoder, UnsafeMutablePointer<Int>) -> OSStatus](./cmsdecodergetnumsigners%28_,_%29.md)
  Obtains the number of signers of a message.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopyallcerts(_:_:))*