# Characteristic Data Formats

**Framework**: HomeKit

Constants for identifying the data format of characteristic values.

#### Overview

Expect to find one of these values in the [`format`](hmcharacteristicmetadata/format.md) property of a characteristic’s metadata.

## Topics

### Booleans
- [let HMCharacteristicMetadataFormatBool: String](hmcharacteristicmetadataformatbool.md)
  Indicates that the characteristic has Boolean values.
### Strings
- [let HMCharacteristicMetadataFormatString: String](hmcharacteristicmetadataformatstring.md)
  Indicates that the characteristic has string values.
### Signed Values
- [let HMCharacteristicMetadataFormatInt: String](hmcharacteristicmetadataformatint.md)
  Indicates that the characteristic has `int` values.
- [let HMCharacteristicMetadataFormatFloat: String](hmcharacteristicmetadataformatfloat.md)
  Indicates that the characteristic has `float` values.
### Unsigned Integers
- [let HMCharacteristicMetadataFormatUInt8: String](hmcharacteristicmetadataformatuint8.md)
  Indicates that the characteristic has unsigned 8-bit integer values.
- [let HMCharacteristicMetadataFormatUInt16: String](hmcharacteristicmetadataformatuint16.md)
  Indicates that the characteristic has unsigned 16-bit integer values.
- [let HMCharacteristicMetadataFormatUInt32: String](hmcharacteristicmetadataformatuint32.md)
  Indicates that the characteristic has unsigned 32-bit integer values.
- [let HMCharacteristicMetadataFormatUInt64: String](hmcharacteristicmetadataformatuint64.md)
  Indicates that the characteristic has unsigned 64-bit integer values.
### Data
- [let HMCharacteristicMetadataFormatData: String](hmcharacteristicmetadataformatdata.md)
  Indicates that the characteristic has data blob values.
- [let HMCharacteristicMetadataFormatTLV8: String](hmcharacteristicmetadataformattlv8.md)
  Indicates that the characteristic has TLV8 values.
### Collections
- [let HMCharacteristicMetadataFormatArray: String](hmcharacteristicmetadataformatarray.md)
  Indicates that the characteristic has array values.
- [let HMCharacteristicMetadataFormatDictionary: String](hmcharacteristicmetadataformatdictionary.md)
  Indicates that the characteristic has dictionary values.

## See Also

- [var format: String?](hmcharacteristicmetadata/format.md)
  The format of the values for the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/characteristic-data-formats)*