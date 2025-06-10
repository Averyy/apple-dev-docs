# vDSP_vswap

**Framework**: Accelerate  
**Kind**: func

Swaps the elements of two single-precision vectors using the specified stride.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vswap(float * __A, vDSP_Stride __IA, float * __B, vDSP_Stride __IB, vDSP_Length __N);
```

#### Discussion

The following code swaps the elements in `vectorA` with those in `vectorB`:

```swift
    var vectorA: [Float] = [1, 3, 5, 7]
    var vectorB: [Float] = [2, 4, 6, 8]
    
    let stride = 1
    let n = vDSP_Length(4)
    
    vDSP_vswap(&vectorA, stride,
               &vectorB, stride,
               n)
    
    print(vectorA) // Prints "[2.0, 4.0, 6.0, 8.0]".
    print(vectorB) // Prints "[1.0, 3.0, 5.0, 7.0]".
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__B`: The output vector.
- `__IB`: The distance between the elements in the output vector.
- `__N`: The number of elements that the operation swaps.

## See Also

- [vDSP_vswapD](vdsp_vswapd.md)
  Swaps the elements of two double-precision vectors using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vswap)*