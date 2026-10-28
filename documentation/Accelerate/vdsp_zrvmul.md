# vDSP_zrvmul

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies a single-precision complex vector by a single-precision real vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_zrvmul(const DSPSplitComplex *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function calculates the products of the first `N` complex elements of `A` to the corresponding real elements of `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvadd function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3213978@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] * B[n];
```

The following code shows an example of using [`vDSP_zrvadd`](./vdsp_zrvadd.md):

**Swift**:

```swift
let n = vDSP_Length(4)
let stride = vDSP_Stride(1)

var realA: [Float] = [2, 4, 8, 16]
var imagA: [Float] = [10, 11, 12, 13]

var b: [Float] = [1, 2, 3, 4]

var realC = [Float](repeating: .nan, count: Int(n))
var imagC = [Float](repeating: .nan, count: Int(n))

realA.withUnsafeMutableBufferPointer { realAPtr in
    imagA.withUnsafeMutableBufferPointer { imagAPtr in
        realC.withUnsafeMutableBufferPointer { realCPtr in
            imagC.withUnsafeMutableBufferPointer { imagCPtr in
                var a = DSPSplitComplex(realp: realAPtr.baseAddress!,
                                        imagp: imagAPtr.baseAddress!)

                var c = DSPSplitComplex(realp: realCPtr.baseAddress!,
                                        imagp: imagCPtr.baseAddress!)

                vDSP_zrvmul(&a, stride,
                            &b, stride,
                            &c, stride,
                            n)
            }
        }
    }
}

print("real", realC) // Prints "real [2.0, 8.0, 24.0, 64.0]".
print("imag", imagC) // Prints "imag [10.0, 22.0, 36.0, 52.0]".
```

**Objective-C**:

```objc
float realA[4] = {2, 4, 8, 16};
float imagA[4] = {10, 11, 12, 13};
float b[4] = {1, 2, 3, 4};
float realC[4];
float imagC[4];

DSPSplitComplex a = { .realp = realA, .imagp = imagA };
DSPSplitComplex c = { .realp = realC, .imagp = imagC };

vDSP_zrvmul(&a, 1,
            b, 1,
            &c, 1,
            4);

// Prints "real [2, 8, 24, 64]".
//         imag [10, 22, 36, 52]
printf("real [%g, %g, %g, %g]\n", realC[0], realC[1], realC[2], realC[3]);
printf("imag [%g, %g, %g, %g]\n", imagC[0], imagC[1], imagC[2], imagC[3]);
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for `IA`.
- `__B`: Single-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Binary (Complex-Real) Multiplication Operations
- [vDSP_zrvmulD](./vdsp_zrvmuld.md)
  Multiplies a double-precision complex vector by a double-precision real vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvmul)*