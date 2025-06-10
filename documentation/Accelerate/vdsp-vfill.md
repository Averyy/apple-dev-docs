# vDSP_vfill

**Framework**: Accelerate  
**Kind**: func

Populates a single-precision vector with a specified scalar value.

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
extern void vDSP_vfill(const float * __A, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The functions in this group populate a vector with a specified scalar value.

The following code shows how to clear the array c, setting the value of each element to pi:

```swift
let n = vDSP_Length(10)
let stride = vDSP_Stride(1)

var a = Float.pi

var c = [Float](repeating: .nan,
                count: Int(n))

vDSP_vfill(&a,
           &c,
           stride,
           n)

// Prints "[3.1415925, 3.1415925, 3.1415925,
//          3.1415925, 3.1415925, 3.1415925,
//          3.1415925, 3.1415925, 3.1415925,
//          3.1415925]"
print(c)
```

## Parameters

- `__A`: Pointer to single-precision real input scalar.
- `__C`: Single-precision real output vector.
- `__IC`: Address stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vfillD](vdsp_vfilld.md)
  Populates a double-precision vector with a specified scalar value.
- [vDSP_vfilli](vdsp_vfilli.md)
  Populates an integer vector with a specified scalar value.
- [vDSP_zvfill](vdsp_zvfill.md)
  Populates a complex single-precision vector with a specified scalar value.
- [vDSP_zvfillD](vdsp_zvfilld.md)
  Populates a complex double-precision vector with a specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfill)*