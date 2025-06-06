# CMSEncoderSetHasDetachedContent(_:_:)

**Framework**: Security  
**Kind**: func

Specifies whether the signed data is to be separate from the message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderSetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContent: Bool) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A signed CMS message can optionally be sent separately from the signed data. Set `detachedContent` to `TRUE` to indicate that the signed data is to be kept separate from the message.

Encrypted messages, including those that are also signed, cannot use detached content.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](cmsencoderupdatecontent(_:_:_:).md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `detachedContent`:   if the message should exclude the data to be signed. Prior to calling this function, the encoder defaults to   for this setting, indicating that the message contains the data to be signed.

## See Also

- [func CMSEncoderGetHasDetachedContent(CMSEncoder, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](cmsencodergethasdetachedcontent(_:_:).md)
  Indicates whether the message is to have detached content.
- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](cmsencoderupdatecontent(_:_:_:).md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSDecoderSetDetachedContent(CMSDecoder, CFData) -> OSStatus](cmsdecodersetdetachedcontent(_:_:).md)
  Specifies the message’s detached content, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodersethasdetachedcontent(_:_:))*