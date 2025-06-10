# vDSP_dotpr2_s1_15

**Framework**: Accelerate  
**Kind**: func

Calculates the stereo dot product of two fixed-point 1.15 format vectors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_dotpr2_s1_15(const short * __A0, vDSP_Stride __IA0, const short * __A1, vDSP_Stride __IA1, const short * __B, vDSP_Stride __IB, short * __C0, short * __C1, vDSP_Length __N);
```

#### Discussion

This function calculates the stereo dot products of two vectors, using the following operation:

```objc
    sum0 = 0;
    sum1 = 0;
    for (i = 0; i < Length; ++i)
    {
        sum0 += A0[i*A0Stride] * B[i*BStride];
        sum1 += A1[i*A1Stride] * B[i*BStride];
    }
    *C0 = sum0;
    *C1 = sum1;
```

For example, the following code calculates the dot products:

```swift
    let stride = 1
    let n = 3
    
    let a0: [Double] = [ 1.0,  2.0,  3.0]
    let a1: [Double] = [10.0, 20.0, 30.0]
    let b: [Double] = [  4.0,  5.0,  6.0]
    
    var c0 = Double()
    var c1 = Double()
    
    vDSP_dotpr2D(a0, stride,
                a1, stride,
                b, stride,
                &c0,
                &c1,
                vDSP_Length(n))
    
    // Prints "32.0 320.0".
    print(c0, c1)
```

## Parameters

- `__A0`: The input vector   for the first channel.
- `__IA0`: The distance between the elements in the input vector   for the first channel.
- `__A1`: The input vector   for the second channel.
- `__IA1`: The distance between the elements in the input vector   for the first channel.
- `__B`: The input vector   for both channels.
- `__IB`: The distance between the elements in the input vector  .
- `__C0`: On output, the dot product of the input vector   for the first channel and the input vector  .
- `__C1`: On output, the dot product of the input vector   for the second channel and the input vector  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_dotpr2](vdsp_dotpr2.md)
  Calculates the stereo dot product of two single-precision vectors.
- [vDSP_dotpr2D](vdsp_dotpr2d.md)
  Calculates the stereo dot product of two double-precision vectors.
- [vDSP_dotpr2_s8_24](vdsp_dotpr2_s8_24.md)
  Calculates the stereo dot product of two fixed-point 8.24 format vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dotpr2_s1_15)*