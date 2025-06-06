# CMSEncoderAddSigners(_:_:)

**Framework**: Security  
**Kind**: func

Specifies signers of the message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder, _ signerOrArray: CFTypeRef) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Call this function only if the message is to be signed. You can call this function more than once for the same message.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](cmsencoderupdatecontent(_:_:_:).md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `signerOrArray`: The identity object for the identity of one signer, specified as type  , or a   of identity objects of type .

## See Also

- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](cmsencoderupdatecontent(_:_:_:).md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCopySigners(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](cmsencodercopysigners(_:_:).md)
  Obtains the array of signers specified with the `CMSEncoderAddSigners` function.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSDecoderCopySignerStatus(CMSDecoder, Int, CFTypeRef, Bool, UnsafeMutablePointer<CMSSignerStatus>?, UnsafeMutablePointer<SecTrust?>?, UnsafeMutablePointer<OSStatus>?) -> OSStatus](cmsdecodercopysignerstatus(_:_:_:_:_:_:_:).md)
  Obtains the status of a CMS message’s signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderaddsigners(_:_:))*