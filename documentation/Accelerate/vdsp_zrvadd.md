# vDSP_zrvadd

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Adds a single-precision complex vector to a single-precision real vector.

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
extern void vDSP_zrvadd(const DSPSplitComplex *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the sums of the first `N` complex elements of `A` to the corresponding real elements of `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvadd function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110566@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B[n];
```

The following code shows an example of using [`vDSP_zrvadd`](./vdsp_zrvadd.md):

**Swift**:

```swift
let n = vDSP_Length(4)
let stride = vDSP_Stride(1)

var realA: [Float] = [2, 4, 8, 16]
var imagA: [Float] = [10, 11, 12, 13]

var b: [Float] = [100, 200, 300, 400]

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

                vDSP_zrvadd(&a, stride,
                            &b, stride,
                            &c, stride,
                            n)
            }
        }
    }
}

print("real", realC) // Prints "real [102.0, 204.0, 308.0, 416.0]".
print("imag", imagC) // Prints "imag [10.0, 11.0, 12.0, 13.0]" (imagp is unchanged)
```

**Objective-C**:

```objc
float realA[4] = {2, 4, 8, 16};
float imagA[4] = {10, 11, 12, 13};
float b[4] = {100, 200, 300, 400};
float realC[4];
float imagC[4];

DSPSplitComplex a = { .realp = realA, .imagp = imagA };
DSPSplitComplex c = { .realp = realC, .imagp = imagC };

vDSP_zrvadd(&a, 1,
            b, 1,
            &c, 1,
            4);

// Prints "real [102, 204, 308, 416]".
//         imag [10, 11, 12, 13]
printf("real [%g, %g, %g, %g]\n", realC[0], realC[1], realC[2], realC[3]);
printf("imag [%g, %g, %g, %g]\n", imagC[0], imagC[1], imagC[2], imagC[3]);
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for `A`.
- `__B`: Single-precision real input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Binary (Complex-Real) Addition Operations
- [vDSP_zrvaddD](./vdsp_zrvaddd.md)
  Adds a double-precision complex vector to a double-precision real vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvadd)*