# vDSP_zvfillD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Populates a complex double-precision vector with a specified scalar value.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_zvfillD(const DSPDoubleSplitComplex *__A, const DSPDoubleSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

The functions in this group populate a vector with a specified scalar value.

The following code shows how to clear the array c, setting the value of each element to pi:

**Swift**:

```swift
// The scalar complex value to broadcast: 3 + 4i.
let aReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: 1)
aReal.initialize(repeating: 3)
let aImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: 1)
aImag.initialize(repeating: 4)
var a = DSPDoubleSplitComplex(realp: aReal.baseAddress!,
                              imagp: aImag.baseAddress!)

let cReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: 4)
let cImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: 4)
var c = DSPDoubleSplitComplex(realp: cReal.baseAddress!,
                              imagp: cImag.baseAddress!)

vDSP_zvfillD(&a, &c, 1, 4)

print(Array(cReal)) // Prints "[3.0, 3.0, 3.0, 3.0]".
print(Array(cImag)) // Prints "[4.0, 4.0, 4.0, 4.0]".
```

**Objective-C**:

```objc
// The scalar complex value to broadcast: 3 + 4i.
double aReal[1] = {3};
double aImag[1] = {4};
DSPDoubleSplitComplex a = { .realp = aReal, .imagp = aImag };

double cReal[4];
double cImag[4];
DSPDoubleSplitComplex c = { .realp = cReal, .imagp = cImag };

vDSP_zvfillD(&a, &c, 1, 4);

// Prints "real=[3, 3, 3, 3] imag=[4, 4, 4, 4]".
printf("real=[%g, %g, %g, %g]\n", cReal[0], cReal[1], cReal[2], cReal[3]);
printf("imag=[%g, %g, %g, %g]\n", cImag[0], cImag[1], cImag[2], cImag[3]);
```

## See Also

### Filling Vectors with a Single Scalar Value
- [vDSP_vfill](./vdsp_vfill.md)
  Populates a single-precision vector with a specified scalar value.
- [vDSP_vfillD](./vdsp_vfilld.md)
  Populates a double-precision vector with a specified scalar value.
- [vDSP_vfilli](./vdsp_vfilli.md)
  Populates an integer vector with a specified scalar value.
- [vDSP_zvfill](./vdsp_zvfill.md)
  Populates a complex single-precision vector with a specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvfilld)*