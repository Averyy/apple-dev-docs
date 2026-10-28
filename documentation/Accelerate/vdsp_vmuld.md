# vDSP_vmulD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise product of two vectors, using the specified stride.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vmulD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function calculates the products of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`, as follows:

```c
 for (n = 0; n < N; ++n)
C[n] = A[n] * B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation as three boxes with multiplication signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vectors.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4336910@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = 1
let count = 5

let a: [Double] = [ 1,  2,  3,  4,  5]
let b: [Double] = [10, 20, 30, 40, 50]

let c = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vmulD(a, stride,
               b, stride,
               buffer.baseAddress!, stride,
               vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[10.0, 40.0, 90.0, 160.0, 250.0]".
print(c)
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;
vDSP_Length count = 5;

double a[] = { 1,  2,  3,  4,  5};
double b[] = {10, 20, 30, 40, 50};
double c[5];

vDSP_vmulD(a, stride,
           b, stride,
           c, stride,
           count);

// Prints "[10, 40, 90, 160, 250]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__A`: The first input vector, `A`.
- `__IA`: The distance between the elements in the first input vector.
- `__B`: The second input vector, `B`.
- `__IB`: The distance between the elements in the second input vector.
- `__C`: The output vector, `C`.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Binary multiplication operations
- [vDSP_vmul](./vdsp_vmul.md)
  Calculates the single-precision element-wise product of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmuld)*