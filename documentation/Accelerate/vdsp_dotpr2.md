# vDSP_dotpr2

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the stereo dot product of two single-precision vectors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
void vDSP_dotpr2(const float *__A0, vDSP_Stride __IA0, const float *__A1, vDSP_Stride __IA1, const float *__B, vDSP_Stride __IB, float *__C0, float *__C1, vDSP_Length __N);
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
    
    let a0: [Float] = [ 1.0,  2.0,  3.0]
    let a1: [Float] = [10.0, 20.0, 30.0]
    let b: [Float] = [  4.0,  5.0,  6.0]
    
    var c0 = Float()
    var c1 = Float()
    
    vDSP_dotpr2(a0, stride,
                a1, stride,
                b, stride,
                &c0,
                &c1,
                vDSP_Length(n))
    
    // Prints "32.0 320.0".
    print(c0, c1)
```

The following code shows an example of using this function:

**Swift**:

```swift
var a0: [Float] = [1, 2, 3, 4]
var a1: [Float] = [4, 3, 2, 1]
var b: [Float] = [5, 6, 7, 8]
var c0: Float = 0
var c1: Float = 0

// Calculate the stereo dot product: `a0` with `b`, and `a1` with `b`.
vDSP_dotpr2(a0, 1, a1, 1, b, 1, &c0, &c1, vDSP_Length(b.count))

// Prints "70.0".
print(c0)
// Prints "60.0".
print(c1)
```

**Objective-C**:

```objc
float a0[4] = {1, 2, 3, 4};
float a1[4] = {4, 3, 2, 1};
float b[4] = {5, 6, 7, 8};
float c0;
float c1;

// Calculate the stereo dot product: `a0` with `b`, and `a1` with `b`.
vDSP_dotpr2(a0, 1, a1, 1, b, 1, &c0, &c1, 4);

// Prints "70".
printf("%g\n", c0);
// Prints "60".
printf("%g\n", c1);
```

## Parameters

- `__A0`: The input vector `A` for the first channel.
- `__IA0`: The distance between the elements in the input vector `A` for the first channel.
- `__A1`: The input vector `A` for the second channel.
- `__IA1`: The distance between the elements in the input vector `A` for the first channel.
- `__B`: The input vector `B` for both channels.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C0`: On output, the dot product of the input vector `A` for the first channel and the input vector `B`.
- `__C1`: On output, the dot product of the input vector `A` for the second channel and the input vector `B`.
- `__N`: The number of elements to process.

## See Also

### Stereo dot product calculation
- [vDSP_dotpr2D](./vdsp_dotpr2d.md)
  Calculates the stereo dot product of two double-precision vectors.
- [vDSP_dotpr2_s1_15](./vdsp_dotpr2_s1_15.md)
  Calculates the stereo dot product of two fixed-point 1.15 format vectors.
- [vDSP_dotpr2_s8_24](./vdsp_dotpr2_s8_24.md)
  Calculates the stereo dot product of two fixed-point 8.24 format vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dotpr2)*