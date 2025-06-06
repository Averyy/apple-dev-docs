# CMSDecoderCopyContent(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the message content, if any.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder, _ contentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If the message has detached content, you are responsible for retrieving the content. In that case, you use the [`CMSDecoderSetDetachedContent(_:_:)`](cmsdecodersetdetachedcontent(_:_:).md) function to tell the decoder the location of the content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `contentOut`: On return, points to the message’s content. Returns   if the content is detached. You must use the   function to free this reference when you are finished using it.

## See Also

- [func CMSEncoderSetHasDetachedContent(CMSEncoder, Bool) -> OSStatus](cmsencodersethasdetachedcontent(_:_:).md)
  Specifies whether the signed data is to be separate from the message.
- [func CMSDecoderSetDetachedContent(CMSDecoder, CFData) -> OSStatus](cmsdecodersetdetachedcontent(_:_:).md)
  Specifies the message’s detached content, if any.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](cmsdecoderfinalizemessage(_:).md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopycontent(_:_:))*