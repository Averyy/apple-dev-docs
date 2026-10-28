# CMSEncoderAddSigners(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies signers of the message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder, _ signerOrArray: CFTypeRef) -> OSStatus
```

```c
OSStatus CMSEncoderAddSigners(CMSEncoderRef cmsEncoder, CFTypeRef signerOrArray);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

Call this function only if the message is to be signed. You can call this function more than once for the same message.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](./cmsencoderupdatecontent%28_,_,_%29.md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the `CMSEncoderCreate` function.
- `signerOrArray`: The identity object for the identity of one signer, specified as type `SecIdentityRef`, or a `CFArray` of identity objects of type`SecIdentityRef`.

## See Also

### Related Documentation
- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](./cmsencoderupdatecontent%28_,_,_%29.md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCopySigners(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsencodercopysigners%28_,_%29.md)
  Obtains the array of signers specified with the `CMSEncoderAddSigners` function.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](./cmsencodercreate%28_%29.md)
  Creates a CMSEncoder reference.
- [func CMSDecoderCopySignerStatus(CMSDecoder, Int, CFTypeRef, Bool, UnsafeMutablePointer<CMSSignerStatus>?, UnsafeMutablePointer<SecTrust?>?, UnsafeMutablePointer<OSStatus>?) -> OSStatus](./cmsdecodercopysignerstatus%28_,_,_,_,_,_,_%29.md)
  Obtains the status of a CMS message’s signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderaddsigners(_:_:))*