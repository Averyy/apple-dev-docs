# CMSEncoderGetHasDetachedContent(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Indicates whether the message is to have detached content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContentOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

```c
OSStatus CMSEncoderGetHasDetachedContent(CMSEncoderRef cmsEncoder, Boolean *detachedContentOut);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

This function returns the value specified in `CMSEncoderSetHasDetachedContent` if that function has been called; otherwise it returns `FALSE`.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the `CMSEncoderCreate` function.
- `detachedContentOut`: Returns `TRUE` if the message has detached content.

## See Also

### Related Documentation
- [func CMSEncoderSetHasDetachedContent(CMSEncoder, Bool) -> OSStatus](./cmsencodersethasdetachedcontent%28_,_%29.md)
  Specifies whether the signed data is to be separate from the message.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodergethasdetachedcontent(_:_:))*