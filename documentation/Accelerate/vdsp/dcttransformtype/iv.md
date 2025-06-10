# vDSP.DCTTransformType.IV

**Framework**: Accelerate  
**Kind**: case

A constant that represents a type-IV discrete cosine transform.

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
case IV
```

#### Discussion

The type-IV DCT uses the following operation for a discrete cosine transform:

```c
// `N` is the length given in the setup.
// `h` is the input array that contains real numbers.
// `H` is the output array that contains real numbers.

For 0 <= k < N
    Or[k] = sum(Ir[j] * cos((k+1/2) * (j+1/2) * pi / N, 0 <= j < N)
```

## See Also

- [vDSP.DCTTransformType.II](vdsp/dcttransformtype/ii.md)
  A constant that represents a type-II discrete cosine transform.
- [vDSP.DCTTransformType.III](vdsp/dcttransformtype/iii.md)
  A constant that represents a type-III discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dcttransformtype/iv)*