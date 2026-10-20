# minimumFractionDigits

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The minimum number of digits after the decimal separator.

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
var minimumFractionDigits: Int { get set }
```

```objc
@property NSUInteger minimumFractionDigits;
```

#### Discussion

By default, this property is set to `0`.

The following code demonstrates the effect of setting [`minimumFractionDigits`](./minimumfractiondigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()
numberFormatter.minimumFractionDigits = 0 // default
numberFormatter.string(from: 123.456) // 123
numberFormatter.minimumFractionDigits = 5
numberFormatter.string(from: 123.456) // 123.45600
```

## See Also

### Configuring Integer and Fraction Digits
- [var minimumIntegerDigits: Int](./minimumintegerdigits.md)
  The minimum number of digits before the decimal separator.
- [var maximumIntegerDigits: Int](./maximumintegerdigits.md)
  The maximum number of digits before the decimal separator.
- [var maximumFractionDigits: Int](./maximumfractiondigits.md)
  The maximum number of digits after the decimal separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/minimumfractiondigits)*