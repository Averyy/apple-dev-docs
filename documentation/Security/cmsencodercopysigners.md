# CMSEncoderCopySigners(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the array of signers specified with the `CMSEncoderAddSigners` function.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderCopySigners(_ cmsEncoder: CMSEncoder, _ signersOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `signersOut`: On return, points to an array of identity objects of type   of the signers of the message. If the   function has not been called for this message, this function returns a   array. You must use the   function to free this reference when you are finished using it.

## See Also

- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSEncoderAddSigners(CMSEncoder, CFTypeRef) -> OSStatus](cmsencoderaddsigners(_:_:).md)
  Specifies signers of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercopysigners(_:_:))*