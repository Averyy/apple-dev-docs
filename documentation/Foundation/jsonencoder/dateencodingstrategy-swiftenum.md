# JSONEncoder.DateEncodingStrategy

**Framework**: Foundation  
**Kind**: enum

The formatting strategies available for formatting dates when encoding a date as JSON.

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
enum DateEncodingStrategy
```

## Topics

### Default Formats
- [JSONEncoder.DateEncodingStrategy.deferredToDate](jsonencoder/dateencodingstrategy-swift.enum/deferredtodate.md)
  The strategy that uses formatting from the Date structure.
### Standard Formats
- [JSONEncoder.DateEncodingStrategy.iso8601](jsonencoder/dateencodingstrategy-swift.enum/iso8601.md)
  The strategy that formats dates according to the ISO 8601 and RFC 3339 standards.
### Custom Formats
- [JSONEncoder.DateEncodingStrategy.formatted(_:)](jsonencoder/dateencodingstrategy-swift.enum/formatted(_:).md)
  The strategy that defers formatting settings to a supplied date formatter.
- [case custom((Date, any Encoder) throws -> Void)](jsonencoder/dateencodingstrategy-swift.enum/custom(_:).md)
  The strategy that formats custom dates by calling a user-defined function.
### Epoch Formats
- [JSONEncoder.DateEncodingStrategy.millisecondsSince1970](jsonencoder/dateencodingstrategy-swift.enum/millisecondssince1970.md)
  The strategy that encodes dates in terms of milliseconds since midnight UTC on January 1, 1970.
- [JSONEncoder.DateEncodingStrategy.secondsSince1970](jsonencoder/dateencodingstrategy-swift.enum/secondssince1970.md)
  The strategy that encodes dates in terms of seconds since midnight UTC on January 1, 1970.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dateEncodingStrategy: JSONEncoder.DateEncodingStrategy](jsonencoder/dateencodingstrategy-swift.property.md)
  The strategy used when encoding dates as part of a JSON object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum)*