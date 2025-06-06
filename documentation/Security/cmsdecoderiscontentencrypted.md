# CMSDecoderIsContentEncrypted(_:_:)

**Framework**: Security  
**Kind**: func

Determines whether a CMS message was encrypted.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder, _ isEncryptedOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Note that if the message was encrypted and the decoding succeeded (`CMSDecoderFinalizeMessage` returned `noErr`), then the message was successfully decrypted. Call [`CMSDecoderCopyContent(_:_:)`](cmsdecodercopycontent(_:_:).md) to retrieve the decrypted content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `isEncryptedOut`: Returns   if the message was encrypted.

## See Also

- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSEncoderAddRecipients(CMSEncoder, CFTypeRef) -> OSStatus](cmsencoderaddrecipients(_:_:).md)
  Specifies a message is to be encrypted and specifies the recipients of the message.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](cmsdecoderfinalizemessage(_:).md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecoderiscontentencrypted(_:_:))*