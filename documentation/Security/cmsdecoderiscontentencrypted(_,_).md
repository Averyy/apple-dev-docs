# CMSDecoderIsContentEncrypted(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Determines whether a CMS message was encrypted.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder, _ isEncryptedOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

```c
OSStatus CMSDecoderIsContentEncrypted(CMSDecoderRef cmsDecoder, Boolean *isEncryptedOut);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

Note that if the message was encrypted and the decoding succeeded (`CMSDecoderFinalizeMessage` returned `noErr`), then the message was successfully decrypted. Call [`CMSDecoderCopyContent(_:_:)`](./cmsdecodercopycontent%28_,_%29.md) to retrieve the decrypted content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `isEncryptedOut`: Returns `TRUE` if the message was encrypted.

## See Also

### Related Documentation
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [func CMSEncoderAddRecipients(CMSEncoder, CFTypeRef) -> OSStatus](./cmsencoderaddrecipients%28_,_%29.md)
  Specifies a message is to be encrypted and specifies the recipients of the message.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecoderiscontentencrypted(_:_:))*