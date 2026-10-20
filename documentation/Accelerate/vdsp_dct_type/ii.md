# vDSP_DCT_Type.II

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

A constant that specifies a type II discrete cosine transform.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case II
```

```c
vDSP_DCT_II
```

#### Discussion

The type-II DCT uses the following operation for a discrete cosine transform:

```
// _N_ is the length given in the setup.
// _h_ is the input array that contains real numbers.
// _H_ is the output array that contains real numbers.

For 0 <= k < N
    Or[k] = sum(Ir[j] * cos(k * (j+1/2) * pi / N, 0 <= j < N)
```

## See Also

### Discrete Cosine Transform Types
- [vDSP_DCT_Type.III](./iii.md)
  A constant that specifies a type III discrete cosine transform.
- [vDSP_DCT_Type.IV](./iv.md)
  A constant that specifies a type IV discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dct_type/ii)*