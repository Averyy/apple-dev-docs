# minimumSignificantDigits

**Framework**: Foundation  
**Kind**: property

The minimum number of significant digits for the number formatter.

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
var minimumSignificantDigits: Int { get set }
```

#### Discussion

You must set the [`usesSignificantDigits`](numberformatter/usessignificantdigits.md) property to [`true`](https://developer.apple.com/documentation/swift/true) in order for this property to affect formatting behavior. By default, the minimum number of significant digits is 1.

The following code demonstrates the effect of setting [`minimumSignificantDigits`](numberformatter/minimumsignificantdigits.md) when formatting various numbers:

```swift
var numberFormatter = NumberFormatter()
numberFormatter.usesSignificantDigits = true
numberFormatter.minimumSignificantDigits = 4

numberFormatter.string(from: 123) // 123.0
numberFormatter.string(from: 123.45) // 123.45
numberFormatter.string(from: 100.23) // 100.23
numberFormatter.string(from: 1.2300) // 1.230
numberFormatter.string(from: 0.000123) // 0.0001230
```

## See Also

- [var usesSignificantDigits: Bool](numberformatter/usessignificantdigits.md)
  A Boolean value indicating whether the formatter uses minimum and maximum significant digits when formatting numbers.
- [var maximumSignificantDigits: Int](numberformatter/maximumsignificantdigits.md)
  The maximum number of significant digits for the number formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/minimumsignificantdigits)*