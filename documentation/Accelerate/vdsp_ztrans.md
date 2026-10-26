# vDSP_ztrans

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Divides a complex single-precision vector by a real single-precision vector.

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
extern void vDSP_ztrans(const float *__A, const DSPSplitComplex *__B, const DSPSplitComplex *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the first `N` elements of `A` divided by the corresponding element in `B`, writing the result to `C`:

![](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110560@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = B[n] / A[n];
```

The following code shows an example of using [`vDSP_ztrans`](./vdsp_ztrans.md):

**Swift**:

```swift
let a: [Float] = [10, 20, 30, 40]

let n = vDSP_Length(a.count)

var realB: [Float] = [100, 200, 300, 400]
var imagB: [Float] = [500, 800, 600, 800]

var realC = [Float](repeating: .nan,
                    count: Int(n))
var imagC = [Float](repeating: .nan,
                    count: Int(n))

realB.withUnsafeMutableBufferPointer { realBPtr in
    imagB.withUnsafeMutableBufferPointer { imagBPtr in
        realC.withUnsafeMutableBufferPointer { realCPtr in
            imagC.withUnsafeMutableBufferPointer { imagCPtr in
                
                var b = DSPSplitComplex(realp: realBPtr.baseAddress!,
                                        imagp: imagBPtr.baseAddress!)
                
                var c = DSPSplitComplex(realp: realCPtr.baseAddress!,
                                        imagp: imagCPtr.baseAddress!)
                
                vDSP_ztrans(a,
                            &b,
                            &c,
                            n)
            }
            
        }
    }
}

print("real", realC) // Prints "real [10, 10, 10, 10]".
print("imag", imagC) // Prints "imag [50, 40, 20, 20]".
```

**Objective-C**:

```objc
float a[4] = {10, 20, 30, 40};
vDSP_Length n = 4;

float realB[4] = {100, 200, 300, 400};
float imagB[4] = {500, 800, 600, 800};
DSPSplitComplex b = { .realp = realB, .imagp = imagB };

float realC[4];
float imagC[4];
DSPSplitComplex c = { .realp = realC, .imagp = imagC };

vDSP_ztrans(a,
            &b,
            &c,
            n);

// Prints "real [10, 10, 10, 10]".
printf("real [%g, %g, %g, %g]\n", realC[0], realC[1], realC[2], realC[3]);
// Prints "imag [50, 40, 20, 20]".
printf("imag [%g, %g, %g, %g]\n", imagC[0], imagC[1], imagC[2], imagC[3]);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__B`: Single-precision complex input vector.
- `__C`: Single-precision complex output vector.
- `__N`: The number of elements to process.

## See Also

### Binary Transfer Operations
- [vDSP_ztransD](./vdsp_ztransd.md)
  Divides a complex double-precision vector by a real double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_ztrans)*