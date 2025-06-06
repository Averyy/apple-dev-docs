# CMSEncoderGetHasDetachedContent(_:_:)

**Framework**: Security  
**Kind**: func

Indicates whether the message is to have detached content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContentOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function returns the value specified in `CMSEncoderSetHasDetachedContent` if that function has been called; otherwise it returns `FALSE`.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `detachedContentOut`: Returns   if the message has detached content.

## See Also

- [func CMSEncoderSetHasDetachedContent(CMSEncoder, Bool) -> OSStatus](cmsencodersethasdetachedcontent(_:_:).md)
  Specifies whether the signed data is to be separate from the message.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodergethasdetachedcontent(_:_:))*