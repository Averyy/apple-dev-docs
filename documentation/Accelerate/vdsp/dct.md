# vDSP.DCT

**Framework**: Accelerate  
**Kind**: class

A single-precision discrete cosine transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
class DCT
```

## Topics

### Initializers
- [init?(previous: vDSP.DCT?, count: Int, transformType: vDSP.DCTTransformType)](vdsp/dct/init(previous:count:transformtype:).md)
  Initializes a new discrete cosine transform instance.
### Instance Methods
- [func transform<U>(U) -> [Float]](vdsp/dct/transform(_:).md)
  Returns the single-precision real discrete cosine transform.
- [func transform<U, V>(U, result: inout V)](vdsp/dct/transform(_:result:).md)
  Computes an out-of-place single-precision real discrete cosine transform.

## See Also

- [vDSP.DCTTransformType](vdsp/dcttransformtype.md)
  An enumeration that describes the discrete cosine transform types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dct)*