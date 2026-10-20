# vDSP.DCT

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A single-precision discrete cosine transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
class DCT
```

## Topics

### Initializers
- [init?(previous: vDSP.DCT?, count: Int, transformType: vDSP.DCTTransformType)](./dct/init%28previous,count,transformtype%29.md)
  Initializes a new discrete cosine transform instance.
### Instance Methods
- [func transform<U>(U) -> [Float]](./dct/transform%28_%29.md)
  Returns the single-precision real discrete cosine transform.
- [func transform<U, V>(U, result: inout V)](./dct/transform%28_,result%29.md)
  Computes an out-of-place single-precision real discrete cosine transform.

## See Also

### Objects that Simplify Discrete Cosine Transforms
- [vDSP.DCTTransformType](./dcttransformtype.md)
  An enumeration that describes the discrete cosine transform types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dct)*