# nonConformingFloatEncodingStrategy

**Framework**: Foundation  
**Kind**: property

The strategy used by an encoder when it encounters exceptional floating-point values.

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
var nonConformingFloatEncodingStrategy: JSONEncoder.NonConformingFloatEncodingStrategy { get set }
```

#### Discussion

The default strategy is the [`JSONEncoder.NonConformingFloatEncodingStrategy.throw`](jsonencoder/nonconformingfloatencodingstrategy-swift.enum/throw.md) strategy.

## See Also

- [JSONEncoder.NonConformingFloatEncodingStrategy](jsonencoder/nonconformingfloatencodingstrategy-swift.enum.md)
  The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.property)*