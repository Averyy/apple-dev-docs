# vDSP_zrvsub

**Framework**: Accelerate  
**Kind**: func

Subtracts a single-precision real vector from a single-precision complex vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zrvsub(const DSPSplitComplex * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function subtracts the first `N` real elements of `B` from corresponding complex elements of `A`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zrvsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/2ed939334dc4eec90ac82ba397b942c5/media-3110556%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

The following code shows an example of using [`vDSP_zrvsub`](vdsp_zrvsub.md):

```swift
let n = vDSP_Length(4)
let stride = vDSP_Stride(1)

var realA: [Float] = [2, 4, 8, 16]
var imagA: [Float] = [10, 11, 12, 13]

var b: [Float] = [1, 2, 3, 4]

var realC = [Float](repeating: .nan,
                    count: Int(n))
var imagC = [Float](repeating: .nan,
                    count: Int(n))

realA.withUnsafeMutableBufferPointer { realAPtr in
    imagA.withUnsafeMutableBufferPointer { imagAPtr in
        realC.withUnsafeMutableBufferPointer { realCPtr in
            imagC.withUnsafeMutableBufferPointer { imagCPtr in
                var a = DSPSplitComplex(realp: realAPtr.baseAddress!,
                                         imagp: imagAPtr.baseAddress!)
                
                var c = DSPSplitComplex(realp: realCPtr.baseAddress!,
                                        imagp: imagCPtr.baseAddress!)
                
                vDSP_zrvsub(&a, stride,
                            &b, stride,
                            &c, stride,
                            n)
            }
        }
    }
}

print("real", realC) // Prints "real [1.0, 2.0, 5.0, 12.0]"
print("imag", imagC) // Prints "imag [10.0, 11.0, 12.0, 13.0]" (imagp is unchanged)
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

- [vDSP_zrvsubD](vdsp_zrvsubd.md)
  Subtracts a double-precision real vector from a double-precision complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrvsub)*