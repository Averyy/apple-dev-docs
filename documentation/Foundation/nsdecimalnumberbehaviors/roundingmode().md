# roundingMode()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.

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
func roundingMode() -> NSDecimalNumber.RoundingMode
```

```objc
- (NSRoundingMode) roundingMode;
```

#### Return Value

Returns the current rounding mode. See [`NSDecimalNumber.RoundingMode`](../nsdecimalnumber/roundingmode.md) for possible values.

## See Also

### Related Documentation
- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)
### Rounding
- [func scale() -> Int16](./scale%28%29.md)
  Returns the number of digits allowed after the decimal separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors/roundingmode())*