# vDSP.DCTTransformType.III

**Framework**: Accelerate  
**Kind**: case

A constant that represents a type-III discrete cosine transform.

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
case III
```

#### Discussion

The type-III DCT uses the following operation for a discrete cosine transform:

```None
// `N` is the length given in the setup.
// `h` is the input array that contains real numbers.
// `H` is the output array that contains real numbers.

For 0 <= k < N
    Or[k] = Ir[0]/2
        + sum(Ir[j] * cos((k+1/2) * j * pi / N), 1 <= j < N)
```

## See Also

- [vDSP.DCTTransformType.II](vdsp/dcttransformtype/ii.md)
  A constant that represents a type-II discrete cosine transform.
- [vDSP.DCTTransformType.IV](vdsp/dcttransformtype/iv.md)
  A constant that represents a type-IV discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dcttransformtype/iii)*