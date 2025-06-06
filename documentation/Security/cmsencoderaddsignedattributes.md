# CMSEncoderAddSignedAttributes(_:_:)

**Framework**: Security  
**Kind**: func

Specifies attributes for a signed message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderAddSignedAttributes(_ cmsEncoder: CMSEncoder, _ signedAttributes: CMSSignedAttributes) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Attributes are optional for signed messages. They are not used for other types of CMS messages.  The use of attributes is described in section 2.5 of the S/MIME 3.1 specification.

If you do call this function, you must call it before the first call to the [`CMSEncoderUpdateContent(_:_:_:)`](cmsencoderupdatecontent(_:_:_:).md) function.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `signedAttributes`: Attribute flags as defined in  .

## See Also

- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](cmsencoderupdatecontent(_:_:_:).md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](cmsencodercreate(_:).md)
  Creates a CMSEncoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderaddsignedattributes(_:_:))*