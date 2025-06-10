# vDSP_vrvrs

**Framework**: Accelerate  
**Kind**: func

Performs an in-place reversal of a single-precision vector.

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
extern void vDSP_vrvrs(float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code reverses the elements in the array `values`:

```swift
    var values: [Float] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    let stride = 1
    let n = vDSP_Length(values.count)
    
    vDSP_vrvrs(&values, stride,
               n)

    // Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
    print(values)
```

## Parameters

- `__C`: The vector that the function reverses in-place.
- `__IC`: The distance between the elements in the vector.
- `__N`: The number of elements in the vector.

## See Also

- [vDSP_vrvrsD](vdsp_vrvrsd.md)
  Performs an in-place reversal of a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrvrs)*