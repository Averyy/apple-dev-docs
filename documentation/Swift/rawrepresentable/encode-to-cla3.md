# encode(to:)

**Framework**: Swift  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `UInt16`.

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
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4evma.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-5igsi.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Bool`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4tbh4.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Double`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-21ma8.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Float`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-8horh.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-78oqu.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4pavm.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int8`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-86dqn.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int16`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-7dyeb.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4gohs.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int64`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-9u5rt.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt8`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-27waz.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt32`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-16ame.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt64`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawrepresentable/encode(to:)-cla3)*