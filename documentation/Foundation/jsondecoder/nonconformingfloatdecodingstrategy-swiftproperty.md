# nonConformingFloatDecodingStrategy

**Framework**: Foundation  
**Kind**: property

The strategy used by a decoder when it encounters exceptional floating-point values.

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
var nonConformingFloatDecodingStrategy: JSONDecoder.NonConformingFloatDecodingStrategy { get set }
```

#### Discussion

The default strategy is the [`JSONDecoder.NonConformingFloatDecodingStrategy.throw`](jsondecoder/nonconformingfloatdecodingstrategy-swift.enum/throw.md) strategy.

## See Also

- [JSONDecoder.NonConformingFloatDecodingStrategy](jsondecoder/nonconformingfloatdecodingstrategy-swift.enum.md)
  The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/nonconformingfloatdecodingstrategy-swift.property)*