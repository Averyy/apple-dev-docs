# MTLDataType.rg11b10Float

**Framework**: Metal  
**Kind**: case

A packed 32-bit format with three floating-point color components, two of which are 11-bit values, and one is a 10-bit value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
case rg11b10Float
```

#### Discussion

The 11-bit components for red and green each store five exponent bits and six mantissa bits. The 10-bit blue component stores five exponent bits and five mantissa bits.

> **Note**:  None of the color components have a sign bit.

## See Also

- [MTLDataType.rgb9e5Float](mtldatatype/rgb9e5float.md)
  A packed 32-bit format with three color components, each of which is a 9-bit floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldatatype/rg11b10float)*