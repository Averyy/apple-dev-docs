# currency(code:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a format style to use integer currency notation.

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
static func currency<V>(code: String) -> Self where Self == IntegerFormatStyle<V>.Currency, V : BinaryInteger
```

## Return Value

An integer format style that uses the specified currency code.

## Discussion

Use the dot-notation form of this method when the call point allows the use of [`IntegerFormatStyle`](../integerformatstyle.md). You typically do this when calling the `formatted` methods of types that conform to [`BinaryInteger`](../../Swift/binaryinteger.md).

The following example creates an array of integers, then uses [`formatted(_:)`](../../Swift/binaryinteger/formatted%28_%29-73k3e.md) and the currency style provided by this method to format the integers as US dollars:

```swift
let nums: [Int] = [100, 1000, 10000, 100000, 1000000]
let currencyNums = nums.map { $0.formatted(
    .currency(code:"USD")) } // ["$100.00", "$1,000.00", "$10,000.00", "$100,000.00", "$1,000,000.00"]
```

## Parameters

- `code`: The currency code to use, such as `EUR` or `JPY`. See ISO-4217 for a list of valid codes.

## See Also

### Applying currency styles
- [static func currency<Value>(code: String) -> Self](./currency%28code%29-1yg68.md)
  Returns a format style to use floating-point currency notation.
- [static func currency(code: String) -> Self](./currency%28code%29-6fhr2.md)
  Returns a format style to use decimal currency notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/currency(code:)-is0v)*