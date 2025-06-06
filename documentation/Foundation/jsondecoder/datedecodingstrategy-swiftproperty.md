# dateDecodingStrategy

**Framework**: Foundation  
**Kind**: property

The strategy used when decoding dates from part of a JSON object.

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
var dateDecodingStrategy: JSONDecoder.DateDecodingStrategy { get set }
```

#### Discussion

The default strategy is the [`JSONDecoder.DateDecodingStrategy.deferredToDate`](jsondecoder/datedecodingstrategy-swift.enum/deferredtodate.md) strategy.

## See Also

- [JSONDecoder.DateDecodingStrategy](jsondecoder/datedecodingstrategy-swift.enum.md)
  The strategies available for formatting dates when decoding them from JSON.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.property)*