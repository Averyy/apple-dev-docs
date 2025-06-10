# vDSP_DCT_Type.II

**Framework**: Accelerate  
**Kind**: case

A constant that specifies a type II discrete cosine transform.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case II
```

#### Discussion

The type-II DCT uses the following operation for a discrete cosine transform:

```None
// `N` is the length given in the setup.
// `h` is the input array that contains real numbers.
// `H` is the output array that contains real numbers.

For 0 <= k < N
    Or[k] = sum(Ir[j] * cos(k * (j+1/2) * pi / N, 0 <= j < N)
```

## See Also

- [vDSP_DCT_Type.III](vdsp_dct_type/iii.md)
  A constant that specifies a type III discrete cosine transform.
- [vDSP_DCT_Type.IV](vdsp_dct_type/iv.md)
  A constant that specifies a type IV discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dct_type/ii)*