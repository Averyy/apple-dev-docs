# init(format:lenient:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a parse strategy instance using the specified floating-point format style.

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
init<Value>(format: Format, lenient: Bool = true) where Format == FloatingPointFormatStyle<Value>, Value : BinaryFloatingPoint
```

Available when `Format` conforms to `FormatStyle` and `Format.FormatInput` conforms to `BinaryFloatingPoint`.

## Parameters

- `format`: A configured [`FloatingPointFormatStyle`](../floatingpointformatstyle.md) that describes the string format to parse.
- `lenient`: A Boolean value that indicates whether the parse strategy should permit some discrepencies when parsing. Defaults to `true`.

## See Also

### Creating a floating-point parse strategy
- [init<Value>(format: Format, lenient: Bool)](./init%28format,lenient%29-9g6wm.md)
  Creates a parse strategy instance using the specified floating-point currency format style.
- [init<Value>(format: Format, lenient: Bool)](./init%28format,lenient%29-1nldg.md)
  Creates a parse strategy instance using the specified floating-point percentage format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointparsestrategy/init(format:lenient:)-5nxey)*