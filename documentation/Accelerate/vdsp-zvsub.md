# vDSP_zvsub

**Framework**: Accelerate  
**Kind**: func

Subtracts two single-precision complex vectors.

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
extern void vDSP_zvsub(const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` complex elements of `A` and `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zvsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/2ed939334dc4eec90ac82ba397b942c5/media-3110563%402x.png)

The operation is:

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

The following code shows an example of using [`vDSP_zvsub`](vdsp_zvsub.md):

```swift
let n = vDSP_Length(4)
let stride = vDSP_Stride(1)

var realA: [Float] = [100, 200, 300, 400]
var realB: [Float] = [10, 20, 30, 40]

var imagA: [Float] = [10, 20, 30, 40]
var imagB: [Float] = [4, 3, 2, 1]

var realC = [Float](repeating: .nan,
                    count: Int(n))
var imagC = [Float](repeating: .nan,
                    count: Int(n))

realA.withUnsafeMutableBufferPointer { realAPtr in
    realB.withUnsafeMutableBufferPointer { realBPtr in
        imagA.withUnsafeMutableBufferPointer { imagAPtr in
            imagB.withUnsafeMutableBufferPointer { imagBPtr in
                realC.withUnsafeMutableBufferPointer { realCPtr in
                    imagC.withUnsafeMutableBufferPointer { imagCPtr in
                        
                        var a = DSPSplitComplex(realp: realAPtr.baseAddress!,
                                                imagp: imagAPtr.baseAddress!)]
                        
                        var b = DSPSplitComplex(realp: realBPtr.baseAddress!,
                                                imagp: imagBPtr.baseAddress!)
                        
                        var c = DSPSplitComplex(realp: realCPtr.baseAddress!,
                                                imagp: imagCPtr.baseAddress!)
                        
                        vDSP_zvsub(&a, stride,
                                   &b, stride,
                                   &c, stride,
                                   n)
                    }
                }
            }
        }
    }
}

print("real", realC) // Prints "real [90.0, 180.0, 270.0, 360.0]"
print("imag", imagC) // Prints "imag [6.0, 17.0, 28.0, 39.0]"
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_zvsubD](vdsp_zvsubd.md)
  Subtracts two double-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvsub)*