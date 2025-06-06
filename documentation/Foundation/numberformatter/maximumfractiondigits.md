# maximumFractionDigits

**Framework**: Foundation  
**Kind**: property

The maximum number of digits after the decimal separator.

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
var maximumFractionDigits: Int { get set }
```

#### Discussion

By default, this property is set to `0`.

The following code demonstrates the effect of setting [`maximumFractionDigits`](numberformatter/maximumfractiondigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()

numberFormatter.maximumFractionDigits = 0 // default
numberFormatter.string(from: 123.456) // 123

numberFormatter.maximumFractionDigits = 3
numberFormatter.string(from: 123.456789) // 123.457
```

## See Also

- [var minimumIntegerDigits: Int](numberformatter/minimumintegerdigits.md)
  The minimum number of digits before the decimal separator.
- [var maximumIntegerDigits: Int](numberformatter/maximumintegerdigits.md)
  The maximum number of digits before the decimal separator.
- [var minimumFractionDigits: Int](numberformatter/minimumfractiondigits.md)
  The minimum number of digits after the decimal separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/maximumfractiondigits)*