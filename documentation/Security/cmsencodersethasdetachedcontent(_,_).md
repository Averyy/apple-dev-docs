# CMSEncoderSetHasDetachedContent(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies whether the signed data is to be separate from the message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderSetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContent: Bool) -> OSStatus
```

```c
OSStatus CMSEncoderSetHasDetachedContent(CMSEncoderRef cmsEncoder, Boolean detachedContent);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

A signed CMS message can optionally be sent separately from the signed data. Set `detachedContent` to `TRUE` to indicate that the signed data is to be kept separate from the message.

Encrypted messages, including those that are also signed, cannot use detached content.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](./cmsencoderupdatecontent%28_,_,_%29.md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the [`CMSEncoderCreate(_:)`](./cmsencodercreate%28_%29.md) function.
- `detachedContent`: `TRUE` if the message should exclude the data to be signed. Prior to calling this function, the encoder defaults to `FALSE` for this setting, indicating that the message contains the data to be signed.

## See Also

### Related Documentation
- [func CMSEncoderGetHasDetachedContent(CMSEncoder, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./cmsencodergethasdetachedcontent%28_,_%29.md)
  Indicates whether the message is to have detached content.
- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](./cmsencoderupdatecontent%28_,_,_%29.md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](./cmsencodercreate%28_%29.md)
  Creates a CMSEncoder reference.
- [func CMSDecoderSetDetachedContent(CMSDecoder, CFData) -> OSStatus](./cmsdecodersetdetachedcontent%28_,_%29.md)
  Specifies the message’s detached content, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodersethasdetachedcontent(_:_:))*