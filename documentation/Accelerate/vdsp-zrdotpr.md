# vDSP_zrdotpr

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision dot product of a complex vector and a real vector.

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
extern void vDSP_zrdotpr(const DSPSplitComplex * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const DSPSplitComplex * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the dot product of two vectors, using the following operation:

```objc
C[0] = sum(A[n] * B[n], 0 <= n < N);
```

For example, the following code calculates the dot product of the two vectors `[1, 2, 3]` and `[4, 5, 6]` as `(1*4)+(2*5)+(3*6)=32`:

```swift
    let stride = 1
    let n = 3
    
    let aReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
    _ = aReal.initialize(from: [ 1.0, 2.0, 3.0 ])
    
    let aImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
    _ = aImag.initialize(from: [ 0.0, 0.0, 0.0 ])
    
    var a = DSPSplitComplex(realp: aReal.baseAddress!,
                            imagp: aImag.baseAddress!)
    
    let b: [Float] = [ 4.0, 5.0, 6.0 ]
    
    let cReal = UnsafeMutablePointer<Float>.allocate(capacity: 1)
    let cImag = UnsafeMutablePointer<Float>.allocate(capacity: 1)
    var c = DSPSplitComplex(realp: cReal,
                            imagp: cImag)
    
    
    vDSP_zrdotpr(&a, stride,
                b, stride,
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
- [vDSP_zrdotprD](vdsp_zrdotprd.md)
  Calculates the double-precision dot product of a complex vector and a real vector.
- [vDSP_zidotpr](vdsp_zidotpr.md)
  Calculates the inner product of two single-precision complex vectors.
- [vDSP_zidotprD](vdsp_zidotprd.md)
  Calculates the inner product of two double-precision complex vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zrdotpr)*