# vDSP_zvneg

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the negative value of each element in the supplied complex single-precision vector.

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
extern void vDSP_zvneg(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

For example, the following code calculates the negative values of the elements of an array:

**Swift**:

```swift
let stride = 1
let n = 8

let srcReals = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
_ = srcReals.initialize(from: [-1, 2, -3, 4, -5, 6, -7, 8])

let srcImaginaries = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
_ = srcImaginaries.initialize(from: [ 10, 20, 30, 40, -50, -60, -70, -80])

var srcValues = DSPSplitComplex(realp: srcReals.baseAddress!,
                                imagp: srcImaginaries.baseAddress!)


let dstReals = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
let dstImaginaries = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)

var dstValues = DSPSplitComplex(realp: dstReals.baseAddress!,
                                imagp: dstImaginaries.baseAddress!)

vDSP_zvneg(&srcValues, stride,
           &dstValues, stride,
           vDSP_Length(n))

// Prints "[1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0]".
print(Array(dstReals))

// Prints "[-10.0, -20.0, -30.0, -40.0, 50.0, 60.0, 70.0, 80.0]".
print(Array(dstImaginaries))
```

**Objective-C**:

```objc
float srcRealp[8] = {-1, 2, -3, 4, -5, 6, -7, 8};
float srcImagp[8] = {10, 20, 30, 40, -50, -60, -70, -80};
DSPSplitComplex srcValues = { .realp = srcRealp, .imagp = srcImagp };

float dstRealp[8];
float dstImagp[8];
DSPSplitComplex dstValues = { .realp = dstRealp, .imagp = dstImagp };

vDSP_zvneg(&srcValues, 1, &dstValues, 1, 8);

// Prints "[1, -2, 3, -4, 5, -6, 7, -8]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
      dstRealp[0], dstRealp[1], dstRealp[2], dstRealp[3],
      dstRealp[4], dstRealp[5], dstRealp[6], dstRealp[7]);

// Prints "[-10, -20, -30, -40, 50, 60, 70, 80]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
      dstImagp[0], dstImagp[1], dstImagp[2], dstImagp[3],
      dstImagp[4], dstImagp[5], dstImagp[6], dstImagp[7]);
```

## Parameters

- `__A`: The input vector `A`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__C`: On output, the negative values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector `C`.
- `__N`: The number of elements that the function processes.

## See Also

### Complex vector negation functions
- [vDSP_zvnegD](./vdsp_zvnegd.md)
  Calculates the negative value of each element in the supplied complex double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvneg)*