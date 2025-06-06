# init(from:)

**Framework**: Core ML  
**Kind**: init

Creates a shaped array from a decoder.

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

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](mlshapedarray/encode(to:).md)
  Encode a shaped array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/init(from:))*