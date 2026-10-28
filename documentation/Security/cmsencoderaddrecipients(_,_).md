# CMSEncoderAddRecipients(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies a message is to be encrypted and specifies the recipients of the message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder, _ recipientOrArray: CFTypeRef) -> OSStatus
```

```c
OSStatus CMSEncoderAddRecipients(CMSEncoderRef cmsEncoder, CFTypeRef recipientOrArray);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

Your keychain must contain a certificate that supports encryption for each recipient. You can call this function more than once for the same message.

You can both sign and encrypt the same message; however, you cannot call both this function and the [`CMSEncoderSetHasDetachedContent(_:_:)`](./cmsencodersethasdetachedcontent%28_,_%29.md) function for the same message.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](./cmsencoderupdatecontent%28_,_,_%29.md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the `CMSEncoderCreate` function.
- `recipientOrArray`: Either a single certificate containing a public encryption key for one message recipient, specified as a certificate object (type [`SecCertificate`](./seccertificate.md)), or a set of certificates specified as a [`CFArray`](../CoreFoundation/cfarray.md) of certificate objects.

## See Also

### Related Documentation
- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](./cmsencoderupdatecontent%28_,_,_%29.md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](./cmsencodercreate%28_%29.md)
  Creates a CMSEncoder reference.
- [func CMSEncoderCopyRecipients(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsencodercopyrecipients%28_,_%29.md)
  Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.
- [func CMSDecoderIsContentEncrypted(CMSDecoder, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./cmsdecoderiscontentencrypted%28_,_%29.md)
  Determines whether a CMS message was encrypted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderaddrecipients(_:_:))*