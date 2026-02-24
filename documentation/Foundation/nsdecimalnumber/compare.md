# compare(_:)

**Framework**: Foundation  
**Kind**: method

Compares this decimal number and another.

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
func compare(_ decimalNumber: NSNumber) -> ComparisonResult
```

#### Return Value

`NSOrderedAscending` if the value of `decimalNumber` is greater than the receiver; `NSOrderedSame` if they’re equal; and `NSOrderedDescending` if the value of `decimalNumber` is less than the receiver.

## Parameters

- `decimalNumber`: The number with which to compare the receiver. This value must not be `nil`. If this value is `nil`, the behavior is undefined and may change in future versions of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/compare(_:))*