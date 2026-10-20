# init(from:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates an array slice from the passed decoder.

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
init(from decoder: any Decoder) throws
```

Available when `Scalar` conforms to `MLShapedArrayScalar` and `Decodable`.

## Parameters

- `decoder`: The object that decodes the array slice for initialization.

## See Also

### Encoding and decoding an array slice
- [func encode(to: any Encoder) throws](./encode%28to%29.md)
  Encodes the array slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/init(from:))*