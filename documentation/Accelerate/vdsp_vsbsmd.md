# vDSP_vsbsmD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise product of the difference of two vectors and a scalar value, using the specified stride.

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
extern void vDSP_vsbsmD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise difference of vectors `A` and `B`, multiplies the difference by scalar value `C`, and writes the result to vector `D`, as follows:

```c
 for (n = 0; n < N; ++n)
    D[n] = (A[n] - B[n]) * C;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row frepresents the operation that subtracts B from A, with three boxes, as well as the input scalar C with one box. The third row represents the multiplication operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4387352@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = 1
let count = 5

let a: [Double] = [ 1,  2,  3,  4,  5]
let b: [Double] = [10, 20, 30, 40, 50]
let c: Double = 5

let d = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vsbsmD(a, stride,
                b, stride,
                [c],
                buffer.baseAddress!, stride,
                vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[-45.0, -90.0, -135.0, -180.0, -225.0]".
print(d)
```

**Objective-C**:

```objc
double a[5] = { 1,  2,  3,  4,  5};
double b[5] = {10, 20, 30, 40, 50};
double c = 5;
double d[5];

vDSP_vsbsmD(a, 1, b, 1, &c, d, 1, 5);

// Prints "[-45, -90, -135, -180, -225]".
printf("[%g, %g, %g, %g, %g]\n", d[0], d[1], d[2], d[3], d[4]);
```

## Parameters

- `__A`: The input vector `A` in `D = (A - B) * C`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input vector `B` in `D = (A - B) * C`.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C`: The input scalar value `C` in `D = (A - B) * C`.
- `__D`: The output vector `D` in `D = (A - B) * C`.
- `__ID`: The distance between the elements in the output vector `D`.
- `__N`: The number of elements that the function processes.

## See Also

### Vector-vector-scalar subtract-multiply operations
- [vDSP_vsbsm](./vdsp_vsbsm.md)
  Calculates the single-precision element-wise product of the difference of two vectors and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsbsmd)*