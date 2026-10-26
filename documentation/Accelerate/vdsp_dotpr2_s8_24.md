# vDSP_dotpr2_s8_24

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the stereo dot product of two fixed-point 8.24 format vectors.

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
void vDSP_dotpr2_s8_24(const int *__A0, vDSP_Stride __IA0, const int *__A1, vDSP_Stride __IA1, const int *__B, vDSP_Stride __IB, int *__C0, int *__C1, vDSP_Length __N);
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

The following code shows an example of using this function:

**Swift**:

```swift
var a0: [Int32] = [8388608, 8388608]
var a1: [Int32] = [4194304, 4194304]
var b: [Int32] = [8388608, 8388608]
var c0: Int32 = 0
var c1: Int32 = 0

// Calculate the stereo dot product of fixed-point 8.24 format vectors (8388608 represents 0.5, 4194304 represents 0.25).
vDSP_dotpr2_s8_24(a0, 1, a1, 1, b, 1, &c0, &c1, vDSP_Length(b.count))

// Prints "8388608".
print(c0)
// Prints "4194304".
print(c1)
```

**Objective-C**:

```objc
int a0[2] = {8388608, 8388608};
int a1[2] = {4194304, 4194304};
int b[2] = {8388608, 8388608};
int c0;
int c1;

// Calculate the stereo dot product of fixed-point 8.24 format vectors (8388608 represents 0.5, 4194304 represents 0.25).
vDSP_dotpr2_s8_24(a0, 1, a1, 1, b, 1, &c0, &c1, 2);

// Prints "8388608".
printf("%d\n", c0);
// Prints "4194304".
printf("%d\n", c1);
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
- [vDSP_dotpr2](./vdsp_dotpr2.md)
  Calculates the stereo dot product of two single-precision vectors.
- [vDSP_dotpr2D](./vdsp_dotpr2d.md)
  Calculates the stereo dot product of two double-precision vectors.
- [vDSP_dotpr2_s1_15](./vdsp_dotpr2_s1_15.md)
  Calculates the stereo dot product of two fixed-point 1.15 format vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dotpr2_s8_24)*