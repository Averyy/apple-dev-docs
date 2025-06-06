# minimumIntegerDigits

**Framework**: Foundation  
**Kind**: property

The minimum number of digits before the decimal separator.

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
var minimumIntegerDigits: Int { get set }
```

#### Discussion

By default, this property is set to `0`.

The following code demonstrates the effect of setting [`minimumIntegerDigits`](numberformatter/minimumintegerdigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()

numberFormatter.minimumIntegerDigits = 0 // default
numberFormatter.string(from: 123) // 123

numberFormatter.minimumIntegerDigits = 5
numberFormatter.string(from: 123) // 00123
```

## See Also

- [var maximumIntegerDigits: Int](numberformatter/maximumintegerdigits.md)
  The maximum number of digits before the decimal separator.
- [var minimumFractionDigits: Int](numberformatter/minimumfractiondigits.md)
  The minimum number of digits after the decimal separator.
- [var maximumFractionDigits: Int](numberformatter/maximumfractiondigits.md)
  The maximum number of digits after the decimal separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/minimumintegerdigits)*