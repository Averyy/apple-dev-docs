# BNNS.PaddingMode

**Framework**: Accelerate  
**Kind**: enum

Constants that define padding modes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
enum PaddingMode
```

## Topics

### Enumeration Cases
- [BNNS.PaddingMode.constantBitPattern(_:)](bnns/paddingmode/constantbitpattern(_:).md)
  A constant that indicates that a padding operation fills the padded area with a specified bit pattern.
- [BNNS.PaddingMode.constantScalar(_:)](bnns/paddingmode/constantscalar(_:).md)
  A constant that indicates that a padding operation fills the padded area with a specified scalar value.
- [BNNS.PaddingMode.reflect](bnns/paddingmode/reflect.md)
  A constant that indicates that a padding operation fills the padded area to form an odd-symmetric pattern.
- [BNNS.PaddingMode.symmetric](bnns/paddingmode/symmetric.md)
  A constant that indicates that a padding operation fills the padded area to form an even-symmetric pattern.
### Instance Properties
- [var bnnsPaddingMode: BNNSPaddingMode](bnns/paddingmode/bnnspaddingmode.md)
  The underlying padding mode structure.
- [var paddingBitPattern: UInt32](bnns/paddingmode/paddingbitpattern.md)
  The padding bit pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/paddingmode)*