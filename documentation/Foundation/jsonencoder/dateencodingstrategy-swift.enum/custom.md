# JSONEncoder.DateEncodingStrategy.custom(_:)

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
case custom((Date, any Encoder) throws -> Void)
```

#### Discussion

If the user-defined function throws, the error propagates upward.

If the user-defined function doesn’t perform any encoding at all, the encoder produces an empty JSON object instead.

## Parameters

- `custom`: A closure that receives the data to encode and the encoder instance to encode to.

## See Also

- [JSONEncoder.DateEncodingStrategy.formatted(_:)](jsonencoder/dateencodingstrategy-swift.enum/formatted(_:).md)
  The strategy that defers formatting settings to a supplied date formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum/custom(_:))*