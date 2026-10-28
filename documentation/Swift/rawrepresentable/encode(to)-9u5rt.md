# encode(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Encodes this value into the given encoder, when the type’s `RawValue` is `UInt8`.

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

Available when `Self` conforms to `Encodable` and `RawValue` is `UInt8`.

## Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

### Encoding a Value
- [func encode(to: any Encoder) throws](./encode%28to%29-4evma.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [func encode(to: any Encoder) throws](./encode%28to%29-5igsi.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Bool`.
- [func encode(to: any Encoder) throws](./encode%28to%29-4tbh4.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Double`.
- [func encode(to: any Encoder) throws](./encode%28to%29-21ma8.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Float`.
- [func encode(to: any Encoder) throws](./encode%28to%29-8horh.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [func encode(to: any Encoder) throws](./encode%28to%29-78oqu.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt`.
- [func encode(to: any Encoder) throws](./encode%28to%29-4pavm.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int8`.
- [func encode(to: any Encoder) throws](./encode%28to%29-86dqn.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int16`.
- [func encode(to: any Encoder) throws](./encode%28to%29-7dyeb.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
- [func encode(to: any Encoder) throws](./encode%28to%29-4gohs.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int64`.
- [func encode(to: any Encoder) throws](./encode%28to%29-cla3.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt16`.
- [func encode(to: any Encoder) throws](./encode%28to%29-27waz.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt32`.
- [func encode(to: any Encoder) throws](./encode%28to%29-16ame.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt64`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawrepresentable/encode(to:)-9u5rt)*