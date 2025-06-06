# CMSEncoderCopySupportingCerts(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the certificates added to a message with `CMSEncoderAddSupportingCerts`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderCopySupportingCerts(_ cmsEncoder: CMSEncoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

A CMS message can contain arbitrary sets of certificates other than or in addition to those indicating the identity of signers. You can use this function to obtain any such certificates added with the `CMSEncoderAddSupportingCerts` function.  If `CMSEncoderAddSupportingCerts` has not been called, this function returns a `NULL` value for `certsOut`. Note that this function does not return the signing certificates, if any.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `certsOut`: On return, points to a CFArray of   objects. You must use the   function to free this reference when you are finished using it.

## See Also

- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSEncoderAddSupportingCerts(CMSEncoder, CFTypeRef) -> OSStatus](cmsencoderaddsupportingcerts(_:_:).md)
  Adds certificates to a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercopysupportingcerts(_:_:))*