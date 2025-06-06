# dateEncodingStrategy

**Framework**: Foundation  
**Kind**: property

The strategy used when encoding dates as part of a JSON object.

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
var dateEncodingStrategy: JSONEncoder.DateEncodingStrategy { get set }
```

#### Discussion

The default strategy is the [`JSONEncoder.DateEncodingStrategy.deferredToDate`](jsonencoder/dateencodingstrategy-swift.enum/deferredtodate.md) strategy.

## See Also

- [JSONEncoder.DateEncodingStrategy](jsonencoder/dateencodingstrategy-swift.enum.md)
  The formatting strategies available for formatting dates when encoding a date as JSON.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/dateencodingstrategy-swift.property)*