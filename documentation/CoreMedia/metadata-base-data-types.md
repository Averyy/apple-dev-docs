# Metadata Base Data Types

**Framework**: Core Media

Constants that describe metadata base data types.

## Topics

### Constants
- [let kCMMetadataBaseDataType_RawData: CFString](kcmmetadatabasedatatype_rawdata.md)
  A sequence of bytes whose interpretation based upon an agreement between the reader and the writer.
- [let kCMMetadataBaseDataType_UTF8: CFString](kcmmetadatabasedatatype_utf8.md)
  UTF-8 string.
- [let kCMMetadataBaseDataType_UTF16: CFString](kcmmetadatabasedatatype_utf16.md)
  UTF-16 string.
- [let kCMMetadataBaseDataType_GIF: CFString](kcmmetadatabasedatatype_gif.md)
  GIF image.
- [let kCMMetadataBaseDataType_JPEG: CFString](kcmmetadatabasedatatype_jpeg.md)
  JPEG image.
- [let kCMMetadataBaseDataType_PNG: CFString](kcmmetadatabasedatatype_png.md)
  PNG image.
- [let kCMMetadataBaseDataType_BMP: CFString](kcmmetadatabasedatatype_bmp.md)
  BMP image.
- [let kCMMetadataBaseDataType_Float32: CFString](kcmmetadatabasedatatype_float32.md)
  32-bit big endian floating point number.
- [let kCMMetadataBaseDataType_Float64: CFString](kcmmetadatabasedatatype_float64.md)
  64-bit big endian floating point number.
- [let kCMMetadataBaseDataType_SInt8: CFString](kcmmetadatabasedatatype_sint8.md)
  8-bit signed integer.
- [let kCMMetadataBaseDataType_SInt16: CFString](kcmmetadatabasedatatype_sint16.md)
  16-bit big endian signed integer.
- [let kCMMetadataBaseDataType_SInt32: CFString](kcmmetadatabasedatatype_sint32.md)
  32-bit big endian signed integer.
- [let kCMMetadataBaseDataType_SInt64: CFString](kcmmetadatabasedatatype_sint64.md)
  64-bit big endian signed integer.
- [let kCMMetadataBaseDataType_UInt8: CFString](kcmmetadatabasedatatype_uint8.md)
  8-bit unsigned integer.
- [let kCMMetadataBaseDataType_UInt16: CFString](kcmmetadatabasedatatype_uint16.md)
  16-bit big endian unsigned integer.
- [let kCMMetadataBaseDataType_UInt32: CFString](kcmmetadatabasedatatype_uint32.md)
  32-bit big endian unsigned integer.
- [let kCMMetadataBaseDataType_UInt64: CFString](kcmmetadatabasedatatype_uint64.md)
  64-bit big endian unsigned integer.
- [let kCMMetadataBaseDataType_PointF32: CFString](kcmmetadatabasedatatype_pointf32.md)
  Consists of two 32-bit big endian floating point values, the x and y values, respectively.
- [let kCMMetadataBaseDataType_DimensionsF32: CFString](kcmmetadatabasedatatype_dimensionsf32.md)
  Consists of a 32-bit big endian floating point x value followed by a 32-bit floating point y value.
- [let kCMMetadataBaseDataType_RectF32: CFString](kcmmetadatabasedatatype_rectf32.md)
  Consists of four 32-bit big endian floating point values, the origin’s x, origin’s y, width and height values, respectively. May also be interpreted as a 32-bit floating point origin followed by a 32-bit floating point dimension.
- [let kCMMetadataBaseDataType_AffineTransformF64: CFString](kcmmetadatabasedatatype_affinetransformf64.md)
  A type that identifies a 3x3 matrix of 64-bit big endian floating point numbers in a row-major order that specify an affine transform.
- [let kCMMetadataBaseDataType_PerspectiveTransformF64: CFString](kcmmetadatabasedatatype_perspectivetransformf64.md)
  A 3x3 matrix of 64-bit big endian floating point numbers the system stores in row-major order that specify a perspective transform.
- [let kCMMetadataBaseDataType_PolygonF32: CFString](kcmmetadatabasedatatype_polygonf32.md)
  Three or more pairs of 32-bit floating point numbers (x and y values) that define the vertices of a polygon.
- [let kCMMetadataBaseDataType_PolylineF32: CFString](kcmmetadatabasedatatype_polylinef32.md)
  Two or more pairs of 32-bit floating point numbers (x and y values) that define a multi-segmented line.
- [let kCMMetadataBaseDataType_JSON: CFString](kcmmetadatabasedatatype_json.md)
  UTF-8 encoded JSON data.

## See Also

- [Metadata Identifier Error Codes](metadata-identifier-errors.md)
  Error codes that indicate metadata identifier errors.
- [Metadata Registry Error Codes](metadata-registry-errors.md)
  Error codes that indicate metadata registry errors.
- [Metadata Identifier Keyspaces](metadata-identifier-keyspaces.md)
  Constants that describe metadata identifier keyspaces.
- [Metadata Identifiers](metadata-identifiers.md)
  Constants that describe metadata identifiers.
- [Metadata Data Types](metadata-data-types.md)
  Constants that describe metadata data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/metadata-base-data-types)*