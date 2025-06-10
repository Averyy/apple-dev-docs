# JSONDecoder.DateDecodingStrategy

**Framework**: Foundation  
**Kind**: enum

The strategies available for formatting dates when decoding them from JSON.

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
enum DateDecodingStrategy
```

## Topics

### Default Formats
- [JSONDecoder.DateDecodingStrategy.deferredToDate](jsondecoder/datedecodingstrategy-swift.enum/deferredtodate.md)
  The strategy that uses formatting from the Date structure.
### Standard Formats
- [JSONDecoder.DateDecodingStrategy.iso8601](jsondecoder/datedecodingstrategy-swift.enum/iso8601.md)
  The strategy that formats dates according to the ISO 8601 standard.
### Custom Formats
- [JSONDecoder.DateDecodingStrategy.formatted(_:)](jsondecoder/datedecodingstrategy-swift.enum/formatted(_:).md)
  The strategy that defers formatting settings to a supplied date formatter.
- [JSONDecoder.DateDecodingStrategy.custom(_:)](jsondecoder/datedecodingstrategy-swift.enum/custom(_:).md)
  The strategy that formats custom dates by calling a user-defined function.
### Epoch Formats
- [JSONDecoder.DateDecodingStrategy.millisecondsSince1970](jsondecoder/datedecodingstrategy-swift.enum/millisecondssince1970.md)
  The strategy that decodes dates in terms of milliseconds since midnight UTC on January 1st, 1970.
- [JSONDecoder.DateDecodingStrategy.secondsSince1970](jsondecoder/datedecodingstrategy-swift.enum/secondssince1970.md)
  The strategy that decodes dates in terms of seconds since midnight UTC on January 1st, 1970.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dateDecodingStrategy: JSONDecoder.DateDecodingStrategy](jsondecoder/datedecodingstrategy-swift.property.md)
  The strategy used when decoding dates from part of a JSON object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum)*