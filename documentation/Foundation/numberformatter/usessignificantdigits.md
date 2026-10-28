# usesSignificantDigits

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the formatter uses minimum and maximum significant digits when formatting numbers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var usesSignificantDigits: Bool { get set }
```

```objc
@property BOOL usesSignificantDigits;
```

## Discussion

The [`NumberFormatter`](../numberformatter.md) class has two ways of determining how many digits to represent:_ _using integer and fraction digits and using significant digits.

When this property is set to [`false`](../../Swift/false.md), numbers are formatted according to whether you want them formatted as fractions or as integers. For more information, see Configuring Integer and Fraction Digits. This property is [`false`](../../Swift/false.md) by default.

Set this property to [`true`](../../Swift/true.md) to format numbers according to the significant digits configuration specified by the [`minimumSignificantDigits`](./minimumsignificantdigits.md) and [`maximumSignificantDigits`](./maximumsignificantdigits.md) properties. By default, the minimum number of significant digits is 1, and the maximum number of significant digits is 6.

> **Note**:  When a number formatter is configured to use significant digits, it ignores any minimum or maximum values used to set integer or fraction digits.

The following code demonstrates the effect of configuring [`usesSignificantDigits`](./usessignificantdigits.md) when formatting various numbers:

```swift
var numberFormatter = NumberFormatter()

// Using significant digits
numberFormatter.usesSignificantDigits = true
numberFormatter.string(from: 12345678) // 12345700
numberFormatter.string(from: 1234.5678) // 1234.57
numberFormatter.string(from: 100.2345678) // 100.235
numberFormatter.string(from: 1.230000) // 1.23
numberFormatter.string(from: 0.00000123) // 0.00000123

// Using integer and fraction digits
numberFormatter.usesSignificantDigits = false
numberFormatter.string(from: 12345678) // 12345678
numberFormatter.string(from: 1234.5678) // 1235
numberFormatter.string(from: 100.2345678) // 100
numberFormatter.string(from: 1.230000) // 1
numberFormatter.string(from: 0.00000123) // 0
```

## See Also

### Configuring Significant Digits
- [var minimumSignificantDigits: Int](./minimumsignificantdigits.md)
  The minimum number of significant digits for the number formatter.
- [var maximumSignificantDigits: Int](./maximumsignificantdigits.md)
  The maximum number of significant digits for the number formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/usessignificantdigits)*