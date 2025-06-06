# init(factor:)

**Framework**: Create ML Components  
**Kind**: init

Creates a down sample temporal transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init(factor: Int)
```

#### Discussion

> **Note**: `factor` must be greater than 0.

`factor` must be greater than 0.

## Parameters

- `factor`: The down sample factor to the input stream.

## See Also

- [init(from: any Decoder) throws](downsampler/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/init(factor:))*