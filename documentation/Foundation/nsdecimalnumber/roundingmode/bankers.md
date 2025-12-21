# NSDecimalNumber.RoundingMode.bankers

**Framework**: Foundation  
**Kind**: case

Round to the closest possible return value; when halfway between two possibilities, return the possibility whose last digit is even.

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
case bankers
```

#### Discussion

In practice, this means that, over the long run, numbers will be rounded up as often as they are rounded down; there will be no systematic bias.

## See Also

- [NSDecimalNumber.RoundingMode.plain](nsdecimalnumber/roundingmode/plain.md)
  Round to the closest possible return value; when caught halfway between two positive numbers, round up; when caught between two negative numbers, round down.
- [NSDecimalNumber.RoundingMode.down](nsdecimalnumber/roundingmode/down.md)
  Round return values down.
- [NSDecimalNumber.RoundingMode.up](nsdecimalnumber/roundingmode/up.md)
  Round return values up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/roundingmode/bankers)*