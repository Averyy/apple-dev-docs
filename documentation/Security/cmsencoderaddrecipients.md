# CMSEncoderAddRecipients(_:_:)

**Framework**: Security  
**Kind**: func

Specifies a message is to be encrypted and specifies the recipients of the message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder, _ recipientOrArray: CFTypeRef) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Your keychain must contain a certificate that supports encryption for each recipient. You can call this function more than once for the same message.

You can both sign and encrypt the same message; however, you cannot call both this function and the [`CMSEncoderSetHasDetachedContent(_:_:)`](cmsencodersethasdetachedcontent(_:_:).md) function for the same message.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](cmsencoderupdatecontent(_:_:_:).md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `recipientOrArray`: Either a single certificate containing a public encryption key for one message recipient, specified as a certificate object (type  ), or a set of certificates specified as a   of certificate objects.

## See Also

- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](cmsencoderupdatecontent(_:_:_:).md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSEncoderCopyRecipients(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](cmsencodercopyrecipients(_:_:).md)
  Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.
- [func CMSDecoderIsContentEncrypted(CMSDecoder, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](cmsdecoderiscontentencrypted(_:_:).md)
  Determines whether a CMS message was encrypted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderaddrecipients(_:_:))*