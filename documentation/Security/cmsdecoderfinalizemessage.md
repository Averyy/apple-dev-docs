# CMSDecoderFinalizeMessage(_:)

**Framework**: Security  
**Kind**: func

Indicates that there is no more data to decode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderFinalizeMessage(_ cmsDecoder: CMSDecoder) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Returns [`errSecUnknownFormat`](errsecunknownformat.md) upon detection of an improperly formatted CMS message.

#### Discussion

When you call this function, the decoder finishes decoding the message. If the message was encrypted and this function returns a result code of `noErr`, the message was successfully decrypted. Call the [`CMSDecoderCopyContent(_:_:)`](cmsdecodercopycontent(_:_:).md) function to retrieve the message content. Call the [`CMSDecoderGetNumSigners(_:_:)`](cmsdecodergetnumsigners(_:_:).md) function to find out if the message was signed and, if so, how many signers there were.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.

## See Also

- [func CMSDecoderGetNumSigners(CMSDecoder, UnsafeMutablePointer<Int>) -> OSStatus](cmsdecodergetnumsigners(_:_:).md)
  Obtains the number of signers of a message.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSDecoderCopyContent(CMSDecoder, UnsafeMutablePointer<CFData?>) -> OSStatus](cmsdecodercopycontent(_:_:).md)
  Obtains the message content, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecoderfinalizemessage(_:))*