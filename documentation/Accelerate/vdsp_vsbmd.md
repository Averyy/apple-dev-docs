# vDSP_vsbmD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise product of a vector and the differences of two vectors, using the specified stride.

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
extern void vDSP_vsbmD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, const double *__C, vDSP_Stride __IC, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function calculates the differences of the first `N` elements of `A` and `B`, multiplies each difference by the corresponding value in `C`, and writes the result to `D`, as follows:

```c
 for (n = 0; n < N; ++n)
    D[n] = (A[n] - B[n]) * C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row represents the operation that subtracts B from A, as well as the input vector C, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337006@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = 1
let count = 5

let a: [Double] = [ 1,  2,  3,  4,  5]
let b: [Double] = [10, 20, 30, 40, 50]
let c: [Double] = [ 5,  4,  3,  2,  1]

let d = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vsbmD(a, stride,
               b, stride,
               c, stride,
               buffer.baseAddress!, stride,
               vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[-45.0, -72.0, -81.0, -72.0, -45.0]".
print(d)
```

**Objective-C**:

```objc
double a[5] = { 1,  2,  3,  4,  5};
double b[5] = {10, 20, 30, 40, 50};
double c[5] = { 5,  4,  3,  2,  1};
double d[5];

vDSP_vsbmD(a, 1, b, 1, c, 1, d, 1, 5);

// Prints "[-45, -72, -81, -72, -45]".
printf("[%g, %g, %g, %g, %g]\n", d[0], d[1], d[2], d[3], d[4]);
```

## Parameters

- `__A`: The input vector `A` in `D = (A - B) * C`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input vector `B` in `D = (A - B) * C`.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C`: The input vector `C` in `D = (A - B) * C`.
- `__IC`: The distance between the elements in the input vector `C`.
- `__D`: The output vector `D` in `D = (A - B) * C`.
- `__ID`: The distance between the elements in the output vector `D`.
- `__N`: The number of elements that the function processes.

## See Also

### Ternary subtract-multiply operations
- [vDSP_vsbm](./vdsp_vsbm.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsbmd)*