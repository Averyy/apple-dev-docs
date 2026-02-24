# CMSEncoderCopyRecipients(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderCopyRecipients(_ cmsEncoder: CMSEncoder, _ recipientsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the [`CMSEncoderCreate(_:)`](cmsencodercreate(_:).md) function.
- `recipientsOut`: On return, points to an array of certificate objects of type [`SecCertificate`](seccertificate.md) of the recipients of the message. If the [`CMSEncoderAddRecipients(_:_:)`](cmsencoderaddrecipients(_:_:).md) function has not been called for this message, this function returns a `NULL` array. You must use the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free this reference when you are finished using it.

## See Also

- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSEncoderAddRecipients(CMSEncoder, CFTypeRef) -> OSStatus](cmsencoderaddrecipients(_:_:).md)
  Specifies a message is to be encrypted and specifies the recipients of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercopyrecipients(_:_:))*