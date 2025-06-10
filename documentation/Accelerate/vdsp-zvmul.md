# vDSP_zvmul

**Framework**: Accelerate  
**Kind**: func

Multiplies a single-precision complex vector by the optionally conjugate of another single-precision complex vector.

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
extern void vDSP_zvmul(const DSPSplitComplex * __A, vDSP_Stride __IA, const DSPSplitComplex * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N, int __Conjugate);
```

#### Discussion

This function calculates the products of the first `N` complex (optionally conjugates) of `A` by the corresponding complex elements of `B`, writing the result to `C`:

With `Conjugate` set to `+1`:

![A diagram showing the operation of the vDSP_zvmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/bb036083ebbaa23d737f918b3fdc2ebc/media-3110582%402x.png)

With `Conjugate` set to -`1`:

![A diagram showing the operation of the vDSP_zvmul function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://docs-assets.developer.apple.com/published/a59fed1a1bd2329feca883738d96610b/media-3110555%402x.png)

The operation is:

```swift
If Conjugate is +1:

    for (n = 0; n < N; ++n)
        C[n] = A[n] * B[n];

If Conjugate is -1:

    for (n = 0; n < N; ++n)
        C[n] = conj(A[n]) * B[n];
```

The following code shows an example of using [`vDSP_zvmul`](vdsp_zvmul.md):

```swift
let n = vDSP_Length(2)
let stride = vDSP_Stride(1)

var realA: [Float] = [10, 100]
var imagA: [Float] = [20, 200]

var realB: [Float] = [30, 30]
var imagB: [Float] = [40, 40]

var realC = [Float](repeating: .nan, count: Int(n))
var imagC = [Float](repeating: .nan, count: Int(n))

let conjugation = false

realA.withUnsafeMutableBufferPointer { realAPtr in
    realB.withUnsafeMutableBufferPointer { realBPtr in
        imagA.withUnsafeMutableBufferPointer { imagAPtr in
            imagB.withUnsafeMutableBufferPointer { imagBPtr in
                realC.withUnsafeMutableBufferPointer { realCPtr in
                    imagC.withUnsafeMutableBufferPointer { imagCPtr in
                        
                        var a = DSPSplitComplex(realp: realAPtr.baseAddress!,
                                                imagp: imagAPtr.baseAddress!)
                        
                        var b = DSPSplitComplex(realp: realBPtr.baseAddress!,
                                                imagp: imagBPtr.baseAddress!)
                        
                        var c = DSPSplitComplex(realp: realCPtr.baseAddress!,
                                                imagp: imagCPtr.baseAddress!)
                        vDSP_zvmul(&a, stride,
                                   &b, stride,
                                   &c, stride,
                                   n,
                                   conjugation ? -1 : 1)
                    }
                }
            }
        }
    }
}

print("real", realC) // Prints "real [-500.0, -5000.0]"
print("imag", imagC) // Prints "imag [1000.0, 10000.0]"
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for  .
- `__B`: Single-precision complex input vector.
- `__IB`: Stride for  .
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for  .
- `__N`: The number of elements to process.
- `__Conjugate`: Specifies whether to use conjugate for  .

## See Also

- [vDSP_zvmulD](vdsp_zvmuld.md)
  Multiplies a double-precision complex vector by the optionally conjugate of another double-precision complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvmul)*