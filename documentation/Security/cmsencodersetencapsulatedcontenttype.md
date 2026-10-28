# CMSEncoderSetEncapsulatedContentType

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies an object identifier for the encapsulated data of a signed message.

**Availability**:
- macOS 10.5+ - Deprecated in 10.7

## Declaration

```c
OSStatus CMSEncoderSetEncapsulatedContentType(CMSEncoderRef cmsEncoder, const SecAsn1Oid *eContentType);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

In a signed message, the signed data consists of any type of content (referred to as the *encapsulated content*, because it is encapsulated in the signed data) plus the signature values. You can indicate the content type of the encapsulated data by specifying an object identifier (OID) in the `eContentType` parameter of this function. The default value for the OID (used if this function is not called) is `id-data`. This is the normal encapsulated content type for applications such as S/MIME, which uses it to indicate MIME-encoded content. You can pass any value that is meaningful to your application. Examples of CMS OIDs are listed in [http://www.imc.org/ietf-smime/other-smime-oids.asn](http://www.imc.org/ietf-smime/other-smime-oids.asn).

If you do call this function, you must call it before the first call to the `CMSEncoderUpdateContent` function.

### Special Considerations

Use [`CMSEncoderSetEncapsulatedContentTypeOID(_:_:)`](./cmsencodersetencapsulatedcontenttypeoid%28_,_%29.md) for new development.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the `CMSEncoderCreate` function.
- `eContentType`: The object identifier for the encapsulated data in a signed message.

## See Also

### Related Documentation
- [func CMSDecoderCopyEncapsulatedContentType(CMSDecoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsdecodercopyencapsulatedcontenttype%28_,_%29.md)
  Obtains the object identifier for the encapsulated data of a signed message.
- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](./cmsencoderupdatecontent%28_,_,_%29.md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](./cmsencodercreate%28_%29.md)
  Creates a CMSEncoder reference.
- [func CMSEncoderCopyEncapsulatedContentType(CMSEncoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsencodercopyencapsulatedcontenttype%28_,_%29.md)
  Obtains the object identifier for the encapsulated data of a signed message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodersetencapsulatedcontenttype)*