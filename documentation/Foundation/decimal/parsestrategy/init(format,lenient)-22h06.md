# init(format:lenient:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a parse strategy instance using the specified decimal currency format style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(format: Format, lenient: Bool = true)
```

Available when `Format` is `Decimal.FormatStyle.Currency`.

## Parameters

- `format`: A configured [`Decimal.FormatStyle`](../formatstyle.md) that describes the currency string format to parse.
- `lenient`: A Boolean value that indicates whether the parse strategy should permit some discrepencies when parsing. Defaults to `true`.

## See Also

### Creating a decimal parse strategy
- [init(format: Format, lenient: Bool)](./init%28format,lenient%29-46ix2.md)
  Creates a parse strategy instance using the specified decimal format style.
- [init(format: Format, lenient: Bool)](./init%28format,lenient%29-36ja3.md)
  Creates a parse strategy instance using the specified decimal percentage format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/parsestrategy/init(format:lenient:)-22h06)*