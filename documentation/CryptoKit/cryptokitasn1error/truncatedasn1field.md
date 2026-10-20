# CryptoKitASN1Error.truncatedASN1Field

**Framework**: Apple CryptoKit  
**Kind**: case  
**Role**: Case

An ASN.1 field is truncated.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case truncatedASN1Field
```

## See Also

### Reporting errors
- [CryptoKitASN1Error.invalidASN1IntegerEncoding](./invalidasn1integerencoding.md)
  An ASN.1 integer doesn’t use the minimum number of bytes for its encoding.
- [CryptoKitASN1Error.invalidASN1Object](./invalidasn1object.md)
  The format of the parsed ASN.1 object doesn’t match the format required for the data type being decoded.
- [CryptoKitASN1Error.invalidFieldIdentifier](./invalidfieldidentifier.md)
  The ASN.1 tag for this field is invalid or unsupported.
- [CryptoKitASN1Error.invalidObjectIdentifier](./invalidobjectidentifier.md)
  An ASN.1 object identifier is invalid.
- [CryptoKitASN1Error.invalidPEMDocument](./invalidpemdocument.md)
  The string doesn’t parse as a PEM document.
- [CryptoKitASN1Error.unexpectedFieldType](./unexpectedfieldtype.md)
  The ASN.1 tag for the parsed field doesn’t match the required format.
- [CryptoKitASN1Error.unsupportedFieldLength](./unsupportedfieldlength.md)
  The encoding used for the field length is unsupported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/cryptokitasn1error/truncatedasn1field)*