# encode(to:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Encodes the array slice.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

Available when `Scalar` conforms to `MLShapedArrayScalar` and `Encodable`.

## Parameters

- `encoder`: The object that encodes the array slice.

## See Also

### Encoding and decoding an array slice
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates an array slice from the passed decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/encode(to:))*