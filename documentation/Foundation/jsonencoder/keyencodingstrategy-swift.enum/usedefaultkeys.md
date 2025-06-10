# JSONEncoder.KeyEncodingStrategy.useDefaultKeys

**Framework**: Foundation  
**Kind**: case

A key encoding strategy that doesn’t change key names during encoding.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case useDefaultKeys
```

#### Discussion

The [`JSONEncoder.KeyEncodingStrategy.useDefaultKeys`](jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys.md) strategy is the strategy used if you don’t specify one.

> **Note**:  If you use a nested `CodingKeys` enumeration to define custom key names, this strategy continues to use those names rather than reverting back to the original property names. Nested `CodingKeys` enumerations are described in [`Encoding and Decoding Custom Types`](encoding-and-decoding-custom-types.md).

## See Also

- [JSONEncoder.KeyEncodingStrategy.convertToSnakeCase](jsonencoder/keyencodingstrategy-swift.enum/converttosnakecase.md)
  A key encoding strategy that converts camel-case keys to snake-case keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys)*