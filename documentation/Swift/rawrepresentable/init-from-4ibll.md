# init(from:)

**Framework**: Swift  
**Kind**: init

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init(from: any Decoder) throws](rawrepresentable/init(from:)-5auil.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-5ar5m.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Bool`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-417i8.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Double`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-9u9tp.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Float`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-3hvw1.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-5ktev.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int8`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-2hvc0.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int16`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-114vz.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-29lhi.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int64`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-94955.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt8`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-6z4x4.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt16`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-3arr3.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt32`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-812cy.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt64`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawrepresentable/init(from:)-4ibll)*