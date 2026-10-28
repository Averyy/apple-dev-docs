# scale()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the number of digits allowed after the decimal separator.

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
func scale() -> Int16
```

```objc
- (short) scale;
```

## Return Value

The number of digits allowed after the decimal separator.

## Discussion

This method limits the precision of the values returned by `NSDecimalNumber`’s `decimalNumberBy...` methods. If [`scale()`](./scale%28%29.md) returns a negative value, it affects the digits before the decimal separator as well. If [`scale()`](./scale%28%29.md) returns `NSDecimalNoScale`, the number of digits is unlimited.

Assuming that [`roundingMode()`](./roundingmode%28%29.md) returns `NSRoundPlain`, different values of [`scale()`](./scale%28%29.md) have the following effects on the number 123.456:

| Scale | Return Value |
| --- | --- |
| `NSDecimalNoScale` | 123.456 |
| 2 | 123.45 |
| 0 | 123 |
| –2 | 100 |

## See Also

### Rounding
- [func roundingMode() -> NSDecimalNumber.RoundingMode](./roundingmode%28%29.md)
  Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors/scale())*