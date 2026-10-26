# vDSP_maxv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision maximum value of a vector.

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
extern void vDSP_maxv(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the maximum value of the first `N` elements of input vector `A`, and writes the result to output scalar `C`.

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector, A, with three boxes. The middle row represents the operation a box that contains the maximum function. The bottom row represents the output scalar value C as a  box. The diagram has connecting lines from the input vector to the operation, and from the operation to the output scalar value.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4465874@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c = Float()

vDSP_maxv(a,
          stride,
          &c,
          n)

print("max", c) // Prints "max 3.6".
```

**Objective-C**:

```objc
float a[] = {-1.5f, 2.25f, 3.6f, 0.2f, -0.1f, -4.3f};
vDSP_Stride stride = 1;
vDSP_Length n = 6;

float c = 0.0f;

vDSP_maxv(a, stride, &c, n);

// Prints "max 3.6".
printf("max %g\n", c);
```

## Parameters

- `__A`: The input vector, `A`.
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output scalar value, `C`. If `N` is zero, the function sets `C` to `-infinity`.
- `__N`: The number of elements that the function processes.

## See Also

### Calculating the maximum value of a vector
- [vDSP_maxvD](./vdsp_maxvd.md)
  Calculates the double-precision maximum value of a vector.
- [vDSP_maxmgv](./vdsp_maxmgv.md)
  Calculates the single-precision maximum magnitude of a vector.
- [vDSP_maxmgvD](./vdsp_maxmgvd.md)
  Calculates the double-precision maximum magnitude of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_maxv)*