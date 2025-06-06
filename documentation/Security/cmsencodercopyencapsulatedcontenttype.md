# CMSEncoderCopyEncapsulatedContentType(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the object identifier for the encapsulated data of a signed message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderCopyEncapsulatedContentType(_ cmsEncoder: CMSEncoder, _ eContentTypeOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

In a signed message, the signed data consists of any type of data (the ) plus the signature values. This function returns the object identifier (OID) of the encapsulated content as it was specified with the `CMSEncoderSetEncapsulatedContentType` function.

If the `CMSEncoderSetEncapsulatedContentType` function has not been called for this message, this function returns a  `NULL` pointer.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `eContentTypeOut`: On return, points to the object identifier for the encapsulated data in the signed message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercopyencapsulatedcontenttype(_:_:))*