# vDSP_DCT_Type.III

**Framework**: Accelerate  
**Kind**: case

A constant that specifies a type III discrete cosine transform.

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

- [vDSP_DCT_Type.II](vdsp_dct_type/ii.md)
  A constant that specifies a type II discrete cosine transform.
- [vDSP_DCT_Type.IV](vdsp_dct_type/iv.md)
  A constant that specifies a type IV discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dct_type/iii)*