# CFNumberFormatterGetDecimalInfoForCurrencyCode(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>!, _ roundingIncrement: UnsafeMutablePointer<Double>!) -> Bool
```

#### Return Value

`true` if the information was obtained successfully, otherwise `false` (for example, if the currency code is unknown or the information is not available).

#### Discussion

The returned values are not localized because these are properties of the currency.

## Parameters

- `currencyCode`: A string containing a ISO 4217 3-letter currency code. For example, AUD for Australian Dollars, EUR for Euros.
- `defaultFractionDigits`: Upon return, contains the number of fraction digits that should be displayed for the currency specified by  .
- `roundingIncrement`: Upon return, contains the rounding increment for the currency specified by  , or   if no rounding is done by the currency.

## See Also

- [func CFNumberFormatterCreateNumberFromString(CFAllocator!, CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFOptionFlags) -> CFNumber!](cfnumberformattercreatenumberfromstring(_:_:_:_:_:).md)
  Returns a number object representing a given string.
- [func CFNumberFormatterCreateStringWithNumber(CFAllocator!, CFNumberFormatter!, CFNumber!) -> CFString!](cfnumberformattercreatestringwithnumber(_:_:_:).md)
  Returns a string representation of the given number using the specified number formatter.
- [func CFNumberFormatterCreateStringWithValue(CFAllocator!, CFNumberFormatter!, CFNumberType, UnsafeRawPointer!) -> CFString!](cfnumberformattercreatestringwithvalue(_:_:_:_:).md)
  Returns a string representation of the given number or value using the specified number formatter.
- [func CFNumberFormatterGetValueFromString(CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](cfnumberformattergetvaluefromstring(_:_:_:_:_:).md)
  Returns a number or value representing a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:))*