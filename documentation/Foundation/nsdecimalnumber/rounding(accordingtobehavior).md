# rounding(accordingToBehavior:)

**Framework**: Foundation  
**Kind**: method

Returns a rounded version of the decimal number using the specified rounding behavior.

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
func rounding(accordingToBehavior behavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber
```

#### Discussion

For a description of the different ways of rounding, see the [`roundingMode`](numberformatter/roundingmode-swift.property.md) method in the [`NSDecimalNumberBehaviors`](nsdecimalnumberbehaviors.md) protocol specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/rounding(accordingtobehavior:))*