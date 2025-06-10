# JSONDecoder.DateDecodingStrategy.custom(_:)

**Framework**: Foundation  
**Kind**: case

The strategy that formats custom dates by calling a user-defined function.

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
@preconcurrency
case custom((any Decoder) throws -> Date)
```

## See Also

- [JSONDecoder.DateDecodingStrategy.formatted(_:)](jsondecoder/datedecodingstrategy-swift.enum/formatted(_:).md)
  The strategy that defers formatting settings to a supplied date formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum/custom(_:))*