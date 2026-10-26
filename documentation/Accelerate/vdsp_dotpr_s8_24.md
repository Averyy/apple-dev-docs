# vDSP_dotpr_s8_24

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the dot product of two fixed-point  8.24 format vectors.

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
void vDSP_dotpr_s8_24(const int *__A, vDSP_Stride __IA, const int *__B, vDSP_Stride __IB, int *__C, vDSP_Length __N);
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
    
    let a: [Double] = [1.0, 2.0, 3.0]
    let b: [Double] = [4.0, 5.0, 6.0]
    
    var c = Double()
    
    vDSP_dotprD(a, stride,
                b, stride,
                &c,
                vDSP_Length(n))
    
    // Prints "32.0".
    print(c)
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Int32] = [8388608, 8388608]
var b: [Int32] = [8388608, 8388608]
var c: Int32 = 0

// Calculate the dot product of two fixed-point 8.24 format vectors (8388608 represents 0.5).
vDSP_dotpr_s8_24(a, 1, b, 1, &c, vDSP_Length(a.count))

// Prints "8388608".
print(c)
```

**Objective-C**:

```objc
int a[2] = {8388608, 8388608};
int b[2] = {8388608, 8388608};
int c;

// Calculate the dot product of two fixed-point 8.24 format vectors (8388608 represents 0.5).
vDSP_dotpr_s8_24(a, 1, b, 1, &c, 2);

// Prints "8388608".
printf("%d\n", c);
```

## Parameters

- `__A`: The input vector `A`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input vector `B`.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C`: On output, the dot product of the two vectors.
- `__N`: The number of elements to process.

## See Also

### Dot product calculation
- [vDSP_dotpr](./vdsp_dotpr.md)
  Calculates the dot product of two single-precision vectors.
- [vDSP_dotprD](./vdsp_dotprd.md)
  Calculates the dot product of two double-precision vectors.
- [vDSP_dotpr_s1_15](./vdsp_dotpr_s1_15.md)
  Calculates the dot product of two fixed-point 1.15 format vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dotpr_s8_24)*