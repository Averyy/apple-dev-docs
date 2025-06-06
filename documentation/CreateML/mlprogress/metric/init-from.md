# init(from:)

**Framework**: Create ML  
**Kind**: init

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](mlprogress/metric/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `String`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlprogress/metric/init(from:))*