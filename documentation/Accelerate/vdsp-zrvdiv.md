# vDSP_zrvdiv

**Framework**: Accelerate  
**Kind**: func

Divides a single-precision complex vector by a single-precision real vector.

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
extern void vDSP_zrvdiv(const DSPSplitComplex * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function divides of the first `N` complex elements of `A` by the corresponding real elements of `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvdiv function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/297413dd5127448921730cc9d5e07d31/media-3110557%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

The following code shows an example of using [`vDSP_zrvdiv`](vdsp_zrvdiv.md):

```swift
let n = vDSP_Length(4)
let stride = vDSP_Stride(1)

var realA: [Float] = [15, 30, 45, 60]
var imagA: [Float] = [30, 60, 90, 120]

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
                
                vDSP_zrvdiv(&a, stride,
                            &b, stride,
                            &c, stride,
                            n)
            }
        }
    }
}

print("real", realC) // Prints "real [15.0. 15.0, 15.0, 15.0]"
print("imag", imagC) // Prints "imag [30.0, 30.0, 30.0, 30.0]"
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision real input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zrvdivD](vdsp_zrvdivd.md)
  Divides a double-precision complex vector by a double-precision real vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvdiv)*