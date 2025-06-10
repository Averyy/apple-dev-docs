# vDSP_vclr

**Framework**: Accelerate  
**Kind**: func

Populates a single-precision vector with zeros.

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
extern void vDSP_vclr(float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The [`vDSP_vclr`](vdsp_vclr.md) and [`vDSP_vclrD`](vdsp_vclrd.md) functions populate a vector with zeros.

The following code shows how to clear the array c, setting the value of each element to zero:

```swift
let n = vDSP_Length(10)
let stride = vDSP_Stride(1)

var c = [Float](repeating: .nan,
                count: Int(n))

vDSP_vclr(&c,
          stride,
          n)

// Prints "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
print(c)
```

## Parameters

- `__C`: Single-precision real output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vclrD](vdsp_vclrd.md)
  Populates a double-precision vector with zeros.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vclr)*