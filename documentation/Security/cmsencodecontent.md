# CMSEncodeContent(_:_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Encodes a message and obtains the result in one high-level function call.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CMSEncodeContent(_ signers: CFTypeRef?, _ recipients: CFTypeRef?, _ eContentTypeOID: CFTypeRef?, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafeRawPointer, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If you use this function, you must include content and you must provide valid non-`NULL` input for at least one of the `signers` and `recipients` parameters. You can both encrypt and sign a message; however, you cannot use detached content with an encrypted message. If you want to create a message that contains certificates and no other content, you must use the [`CMSEncoderAddSupportingCerts(_:_:)`](cmsencoderaddsupportingcerts(_:_:).md) function instead of this one. To gain more control over the process of encoding a message, call the sequence of functions beginning with the [`CMSEncoderCreate(_:)`](cmsencodercreate(_:).md) function instead of this one.

## Parameters

- `signers`: The identity object for the identity of one signer, specified as type `SecIdentityRef`, or a `CFArray` of identity objects of type`SecIdentityRef`. Pass `NULL` for this parameter if you do not want to sign the message.
- `recipients`: A certificate containing a public encryption key for one message recipient, specified as a certificate object (type `SecCertificateRef`), or a `CFArray` of certificate objects. Pass NULL for this parameter if you do not want to encrypt the message.
- `eContentTypeOID`: The object identifier for the encapsulated data in a signed message, in the form of a Core Foundation string—`CFSTR("1.2.840.113549.1.7.1")`, for example. This parameter is optional. If you pass `NULL`, the value `id-data` is used. (This is the normal encapsulated content type for applications such as S/MIME, which uses it to indicate MIME-encoded content.) You can pass any value that is meaningful to your application.
- `detachedContent`: Specify `TRUE` if the signed data is to be separate from the message; that is, if the message is_not_ to include the data to be signed. You cannot specify `TRUE` for this parameter for an encrypted message.
- `signedAttributes`: Attribute flags as defined in [`CMSSignedAttributes`](cmssignedattributes.md). Attributes are optional for signed messages and are not used in other types of CMS messages. The use of attributes is described in section 2.5 of the S/MIME 3.1 specification.
- `content`: The content that you want to add to the message. The content must conform to the type set in the [`CMSEncoderSetEncapsulatedContentType`](cmsencodersetencapsulatedcontenttype.md) parameter (or type `id-data` if that function has not been called).
- `contentLen`: The length of the content being added, in bytes.
- `encodedContentOut`: On return, points to the encoded message. You must use the `CFRelease` function to free this reference when you are finished using it.

## See Also

- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.
- [func CMSEncoderAddSupportingCerts(CMSEncoder, CFTypeRef) -> OSStatus](cmsencoderaddsupportingcerts(_:_:).md)
  Adds certificates to a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodecontent(_:_:_:_:_:_:_:_:))*