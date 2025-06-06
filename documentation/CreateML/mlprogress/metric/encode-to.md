# encode(to:)

**Framework**: Create ML  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `String`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [init(from: any Decoder) throws](mlprogress/metric/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlprogress/metric/encode(to:))*