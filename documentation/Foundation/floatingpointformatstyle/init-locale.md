# init(locale:)

**Framework**: Foundation  
**Kind**: init

Creates a floating-point format style that uses the given locale.

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
init(locale: Locale = .autoupdatingCurrent)
```

#### Discussion

Create a [`FloatingPointFormatStyle`](floatingpointformatstyle.md) when you intend to apply a given style to multiple floating-point values. The following example creates a style that uses the `en_US` locale, which uses three-based grouping and comma separators. It then applies this style to all the [`Double`](https://developer.apple.com/documentation/Swift/Double) values in an array.

```swift
let enUSstyle = FloatingPointFormatStyle<Double>(locale: Locale(identifier: "en_US"))
let nums = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let formattedNums = nums.map { enUSstyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]

```

To format a single integer, you can use the [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint) instance method [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint/formatted(_:)-83x4n), passing in an instance of [`FloatingPointFormatStyle`](floatingpointformatstyle.md).

## Parameters

- `locale`: The locale to use when formatting or parsing floating-point values. Defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/init(locale:))*