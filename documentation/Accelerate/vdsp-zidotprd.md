# vDSP_zidotprD

**Framework**: Accelerate  
**Kind**: func

Calculates the inner product of two double-precision complex vectors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_zidotprD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __B, vDSP_Stride __IB, const DSPDoubleSplitComplex * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the dot product of two vectors, using the following operation:

```objc
C[0] = sum(conj(A[n]) * B[n], 0 <= n < N);
```

For example, the following code calculates the dot product of the two vectors `[1, 2, 3]` and `[4, 5, 6]` as `(1*4)+(2*5)+(3*6)=32`:

```swift
    let stride = 1
    let n = 3
    
    let aReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = aReal.initialize(from: [ 1.0, 2.0, 3.0 ])
    
    let aImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = aImag.initialize(from: [ 0.0, 0.0, 0.0 ])
    
    var a = DSPDoubleSplitComplex(realp: aReal.baseAddress!,
                                  imagp: aImag.baseAddress!)
    
    let bReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = bReal.initialize(from: [ 4.0, 5.0, 6.0 ])
    
    let bImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = bImag.initialize(from: [ 0.0, 0.0, 0.0 ])
    
    var b = DSPDoubleSplitComplex(realp: bReal.baseAddress!,
                                  imagp: bImag.baseAddress!)
    
    let cReal = UnsafeMutablePointer<Double>.allocate(capacity: 1)
    let cImag = UnsafeMutablePointer<Double>.allocate(capacity: 1)
    var c = DSPDoubleSplitComplex(realp: cReal,
                                  imagp: cImag)
    
    
    vDSP_zidotprD(&a, stride,
                  &b, stride,
                  &c,
                  vDSP_Length(n))
    
    // Prints "32.0 0.0".
    print(cReal.pointee, cImag.pointee)
```

## Parameters

- `__A`: The input vector  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input vector  .
- `__IB`: The distance between the elements in the input vector  .
- `__C`: On output, the dot product of the two vectors.
- `__N`: The number of elements to process.

## See Also

- [vDSP_zdotpr](vdsp_zdotpr.md)
  Calculates the dot product of two single-precision complex vectors.
- [vDSP_zdotprD](vdsp_zdotprd.md)
  Calculates the dot product of two double-precision complex vectors.
- [vDSP_zrdotpr](vdsp_zrdotpr.md)
  Calculates the single-precision dot product of a complex vector and a real vector.
- [vDSP_zrdotprD](vdsp_zrdotprd.md)
  Calculates the double-precision dot product of a complex vector and a real vector.
- [vDSP_zidotpr](vdsp_zidotpr.md)
  Calculates the inner product of two single-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zidotprd)*