# CMSDecoderCopyEncapsulatedContentType(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the object identifier for the encapsulated data of a signed message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopyEncapsulatedContentType(_ cmsDecoder: CMSDecoder, _ eContentTypeOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

In a signed message, the signed data consists of any type of content (referred to as the , because it is encapsulated in the signed data) plus the signature values. The content type of the encapsulated data is indicated by an object identifier. The default value for the OID is `id-data`, which indicates MIME-encoded content.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `eContentTypeOut`: On return, the object identifier for the encapsulated data in a signed message.  Returns   if the message was not signed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopyencapsulatedcontenttype(_:_:))*