# vDSP_zvsub

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Subtracts two single-precision complex vectors.

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
extern void vDSP_zvsub(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__B, vDSP_Stride __IB, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` complex elements of `A` and `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_zvsub function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110563@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

The following code shows an example of using [`vDSP_zvsub`](./vdsp_zvsub.md):

**Swift**:

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
                                                imagp: imagAPtr.baseAddress!)
                        
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

print("real", realC) // Prints "real [90.0, 180.0, 270.0, 360.0]".
print("imag", imagC) // Prints "imag [6.0, 17.0, 28.0, 39.0]".
```

**Objective-C**:

```objc
float realA[4] = {100, 200, 300, 400};
float imagA[4] = {10, 20, 30, 40};
DSPSplitComplex a = { .realp = realA, .imagp = imagA };

float realB[4] = {10, 20, 30, 40};
float imagB[4] = {4, 3, 2, 1};
DSPSplitComplex b = { .realp = realB, .imagp = imagB };

float realC[4];
float imagC[4];
DSPSplitComplex c = { .realp = realC, .imagp = imagC };

vDSP_zvsub(&a, 1, &b, 1, &c, 1, 4);

// Prints "real [90, 180, 270, 360]".
printf("real [%g, %g, %g, %g]\n", realC[0], realC[1], realC[2], realC[3]);
// Prints "imag [6, 17, 28, 39]".
printf("imag [%g, %g, %g, %g]\n", imagC[0], imagC[1], imagC[2], imagC[3]);
```

## Parameters

- `__A`: Single-precision complex input vector.
- `__IA`: Stride for `A`.
- `__B`: Single-precision complex input vector.
- `__IB`: Stride for `B`.
- `__C`: Single-precision complex output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Binary Subtraction Operations
- [vDSP_zvsubD](./vdsp_zvsubd.md)
  Subtracts two double-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvsub)*