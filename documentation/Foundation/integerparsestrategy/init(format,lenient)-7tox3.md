# init(format:lenient:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a parse strategy instance using the specified integer currency format style.

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
init<Value>(format: Format, lenient: Bool = true) where Format == IntegerFormatStyle<Value>.Currency, Value : BinaryInteger
```

Available when `Format` conforms to `FormatStyle` and `Format.FormatInput` conforms to `BinaryInteger`.

## Parameters

- `format`: A configured [`IntegerFormatStyle.Currency`](../integerformatstyle/currency.md) that describes the currency string format to parse.
- `lenient`: A Boolean value that indicates whether the parse strategy should permit some discrepencies when parsing. Defaults to `true`.

## See Also

### Creating an integer parse strategy
- [init<Value>(format: Format, lenient: Bool)](./init%28format,lenient%29-124xn.md)
  Creates a parse strategy instance using the specified integer format style.
- [init<Value>(format: Format, lenient: Bool)](./init%28format,lenient%29-3gbvo.md)
  Creates a parse strategy instance using the specified integer percentage format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerparsestrategy/init(format:lenient:)-7tox3)*