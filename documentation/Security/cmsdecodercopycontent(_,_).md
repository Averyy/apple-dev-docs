# CMSDecoderCopyContent(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the message content, if any.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder, _ contentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

```c
OSStatus CMSDecoderCopyContent(CMSDecoderRef cmsDecoder, CFDataRef*contentOut);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

If the message has detached content, you are responsible for retrieving the content. In that case, you use the [`CMSDecoderSetDetachedContent(_:_:)`](./cmsdecodersetdetachedcontent%28_,_%29.md) function to tell the decoder the location of the content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `contentOut`: On return, points to the message’s content. Returns `NULL` if the content is detached. You must use the `CFRelease` function to free this reference when you are finished using it.

## See Also

### Related Documentation
- [func CMSEncoderSetHasDetachedContent(CMSEncoder, Bool) -> OSStatus](./cmsencodersethasdetachedcontent%28_,_%29.md)
  Specifies whether the signed data is to be separate from the message.
- [func CMSDecoderSetDetachedContent(CMSDecoder, CFData) -> OSStatus](./cmsdecodersetdetachedcontent%28_,_%29.md)
  Specifies the message’s detached content, if any.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopycontent(_:_:))*