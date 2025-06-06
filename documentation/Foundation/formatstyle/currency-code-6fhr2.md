# currency(code:)

**Framework**: Foundation  
**Kind**: method

Returns a format style to use decimal currency notation.

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
static func currency(code: String) -> Self
```

#### Return Value

A decimal format style that uses the specified currency code.

#### Discussion

Use the dot-notation form of this method when the call point allows the use of [`Decimal.FormatStyle`](decimal/formatstyle.md). You typically do this when calling the [`formatted(_:)`](decimal/formatted(_:).md) method of [`Decimal`](decimal.md).

The following example creates an array of decimals, then uses [`formatted(_:)`](decimal/formatted(_:).md) and the currency style provided by this method to format the values as US dollars.

```swift
let nums: [Decimal] = [100.01, 1000.02, 10000.03, 100000.04, 1000000.05]
let currencyNums = nums.map { $0.formatted(
    .currency(code:"USD")) } // ["$100.01", "$1,000.02", "$10,000.03", "$100,000.04", "$1,000,000.05"]
```

## Parameters

- `code`: The currency code to use, such as   or  . See ISO-4217 for a list of valid codes.

## See Also

- [static func currency<V>(code: String) -> Self](formatstyle/currency(code:)-is0v.md)
  Returns a format style to use integer currency notation.
- [static func currency<Value>(code: String) -> Self](formatstyle/currency(code:)-1yg68.md)
  Returns a format style to use floating-point currency notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/currency(code:)-6fhr2)*