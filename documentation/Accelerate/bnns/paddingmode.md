# BNNS.PaddingMode

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that define padding modes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
enum PaddingMode
```

## Topics

### Enumeration Cases
- [BNNS.PaddingMode.constantBitPattern(_:)](./paddingmode/constantbitpattern%28_%29.md)
  A constant that indicates that a padding operation fills the padded area with a specified bit pattern.
- [BNNS.PaddingMode.constantScalar(_:)](./paddingmode/constantscalar%28_%29.md)
  A constant that indicates that a padding operation fills the padded area with a specified scalar value.
- [BNNS.PaddingMode.reflect](./paddingmode/reflect.md)
  A constant that indicates that a padding operation fills the padded area to form an odd-symmetric pattern.
- [BNNS.PaddingMode.symmetric](./paddingmode/symmetric.md)
  A constant that indicates that a padding operation fills the padded area to form an even-symmetric pattern.
### Instance Properties
- [var bnnsPaddingMode: BNNSPaddingMode](./paddingmode/bnnspaddingmode.md)
  The underlying padding mode structure.
- [var paddingBitPattern: UInt32](./paddingmode/paddingbitpattern.md)
  The padding bit pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/paddingmode)*