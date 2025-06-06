# CMSDecoderSetDetachedContent(_:_:)

**Framework**: Security  
**Kind**: func

Specifies the message’s detached content, if any.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderSetDetachedContent(_ cmsDecoder: CMSDecoder, _ detachedContent: CFData) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The data of a signed CMS message can optionally be sent separately from the message. If the message’s content is detached from the message, you must call this function to tell the decoder where to find the message content.

Encrypted messages, including those that are also signed, cannot use detached content.

You can call this function either before or after decoding the message (by calling the `CMSDecoderUpdateMessage` and `CMSDecoderFinalizeMessage` functions). If a signed message has detached content, however, you must call this function before you can use the `CMSDecoderCopySignerStatus` function to ascertain the signature status.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `detachedContent`: A reference to the message’s detached content.

## See Also

- [func CMSEncoderSetHasDetachedContent(CMSEncoder, Bool) -> OSStatus](cmsencodersethasdetachedcontent(_:_:).md)
  Specifies whether the signed data is to be separate from the message.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSDecoderCopySignerStatus(CMSDecoder, Int, CFTypeRef, Bool, UnsafeMutablePointer<CMSSignerStatus>?, UnsafeMutablePointer<SecTrust?>?, UnsafeMutablePointer<OSStatus>?) -> OSStatus](cmsdecodercopysignerstatus(_:_:_:_:_:_:_:).md)
  Obtains the status of a CMS message’s signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodersetdetachedcontent(_:_:))*