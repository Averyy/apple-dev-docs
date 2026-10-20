# maximumIntegerDigits

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The maximum number of digits before the decimal separator.

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
var maximumIntegerDigits: Int { get set }
```

```objc
@property NSUInteger maximumIntegerDigits;
```

#### Discussion

By default, this property is set to `42`.

The following code demonstrates the effect of setting [`maximumIntegerDigits`](./maximumintegerdigits.md) when formatting a number:

```swift
var numberFormatter = NumberFormatter()

numberFormatter.maximumIntegerDigits = 42 // default
numberFormatter.string(from: 12345) // 12345

numberFormatter.maximumIntegerDigits = 3
numberFormatter.string(from: 12345) // 345
```

## See Also

### Configuring Integer and Fraction Digits
- [var minimumIntegerDigits: Int](./minimumintegerdigits.md)
  The minimum number of digits before the decimal separator.
- [var minimumFractionDigits: Int](./minimumfractiondigits.md)
  The minimum number of digits after the decimal separator.
- [var maximumFractionDigits: Int](./maximumfractiondigits.md)
  The maximum number of digits after the decimal separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/maximumintegerdigits)*