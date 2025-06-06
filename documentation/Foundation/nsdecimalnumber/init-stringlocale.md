# init(string:locale:)

**Framework**: Foundation  
**Kind**: init

Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(string numberValue: String?, locale: Any?)
```

#### Discussion

The locale parameter determines whether the `decimalSeparator` is a period (like in the United States) or a comma (like in France).

The following strings show examples of acceptable values for `numberValue`:

- `2500.6` (or `2500,6`, depending on locale)
- `–2500.6` (or `–2500,6`)
- `–2.5006e3` (or `–2,5006e3`)
- `–2.5006E3` (or `–2,5006E3`)

The following strings are unacceptable:

- `2,500.6`
- `2500 3/5`
- `2.5006x10e3`
- `two thousand five hundred and six tenths`

## Parameters

- `numberValue`: Besides digits,   can include an initial   or  ; a single   or  , to indicate the exponent of a number in scientific notation; and a single decimal separator character to divide the fractional from the integral part of the number.
- `locale`: A dictionary that defines the locale (specifically the  ) to use to interpret the number in  .

## See Also

- [init(decimal: Decimal)](nsdecimalnumber/init(decimal:).md)
  Initializes a decimal number to represent a given decimal.
- [convenience init(mantissa: UInt64, exponent: Int16, isNegative: Bool)](nsdecimalnumber/init(mantissa:exponent:isnegative:).md)
  Initializes a decimal number using the given mantissa, exponent, and sign.
- [convenience init(string: String?)](nsdecimalnumber/init(string:).md)
  Initializes a decimal number so that its value is equivalent to that in a given numeric string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/init(string:locale:))*