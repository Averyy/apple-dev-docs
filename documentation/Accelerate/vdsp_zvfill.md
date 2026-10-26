# vDSP_zvfill

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Populates a complex single-precision vector with a specified scalar value.

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
extern void vDSP_zvfill(const DSPSplitComplex *__A, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The functions in this group populate a vector with a specified scalar value.

The following code shows how to clear the array c, setting the value of each element to pi:

**Swift**:

```swift
let n = vDSP_Length(4)
let stride = vDSP_Stride(1)

// The scalar complex value to broadcast: 3 + 4i.
var aReal: [Float] = [3]
var aImag: [Float] = [4]

var cReal = [Float](repeating: 0, count: Int(n))
var cImag = [Float](repeating: 0, count: Int(n))

aReal.withUnsafeMutableBufferPointer { aRealPtr in
    aImag.withUnsafeMutableBufferPointer { aImagPtr in
        cReal.withUnsafeMutableBufferPointer { cRealPtr in
            cImag.withUnsafeMutableBufferPointer { cImagPtr in

                var a = DSPSplitComplex(realp: aRealPtr.baseAddress!,
                                        imagp: aImagPtr.baseAddress!)

                var c = DSPSplitComplex(realp: cRealPtr.baseAddress!,
                                        imagp: cImagPtr.baseAddress!)

                vDSP_zvfill(&a,
                            &c,
                            stride,
                            n)
            }
        }
    }
}

print("real=\(cReal)") // Prints "real=[3.0, 3.0, 3.0, 3.0]".
print("imag=\(cImag)") // Prints "imag=[4.0, 4.0, 4.0, 4.0]".
```

**Objective-C**:

```objc
// The scalar complex value to broadcast: 3 + 4i.
float aReal[1] = {3};
float aImag[1] = {4};
DSPSplitComplex a = { .realp = aReal, .imagp = aImag };

float cReal[4];
float cImag[4];
DSPSplitComplex c = { .realp = cReal, .imagp = cImag };

vDSP_zvfill(&a, &c, 1, 4);

// Prints "real=[3, 3, 3, 3] imag=[4, 4, 4, 4]".
printf("real=[%g, %g, %g, %g]\n", cReal[0], cReal[1], cReal[2], cReal[3]);
printf("imag=[%g, %g, %g, %g]\n", cImag[0], cImag[1], cImag[2], cImag[3]);
```

## Parameters

- `__A`: Pointer to single-precision complex input scalar.
- `__C`: Single-precision complex output vector.
- `__IC`: Address stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Filling Vectors with a Single Scalar Value
- [vDSP_vfill](./vdsp_vfill.md)
  Populates a single-precision vector with a specified scalar value.
- [vDSP_vfillD](./vdsp_vfilld.md)
  Populates a double-precision vector with a specified scalar value.
- [vDSP_vfilli](./vdsp_vfilli.md)
  Populates an integer vector with a specified scalar value.
- [vDSP_zvfillD](./vdsp_zvfilld.md)
  Populates a complex double-precision vector with a specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvfill)*