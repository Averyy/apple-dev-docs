# vDSP_vmmaD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise sum of the products of two pairs of vectors, using the specified stride.

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
extern void vDSP_vmmaD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, const double *__C, vDSP_Stride __IC, const double *__D, vDSP_Stride __ID, double *__E, vDSP_Stride __IE, vDSP_Length __N);
```

## Discussion

This function calculates the differences of the first `N` elements of the product of vectors `A` and `B` and the product of vectors `C` and `D`, as follows:

```c
 for (n = 0; n < N; ++n)
    E[n] = A[n]*B[n] + C[n]*D[n]; 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that multiply vectors A and B, and multiply vectors C and D, with three boxes of each. The third row represents the addition operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4470528@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = 1
let count = 5

let a: [Double] = [ 1,  2,  3,  4,  5]
let b: [Double] = [10, 20, 30, 40, 50]
let c: [Double] = [ 5,  4,  3,  2,  1]
let d: [Double] = [50, 40, 30, 20, 10]

let e = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vmmaD(a, stride,
               b, stride,
               c, stride,
               d, stride,
               buffer.baseAddress!, stride,
               vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[260.0, 200.0, 180.0, 200.0, 260.0]".
print(e)
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;
vDSP_Length count = 5;

double a[] = { 1,  2,  3,  4,  5};
double b[] = {10, 20, 30, 40, 50};
double c[] = { 5,  4,  3,  2,  1};
double d[] = {50, 40, 30, 20, 10};

double e[5];

vDSP_vmmaD(a, stride,
           b, stride,
           c, stride,
           d, stride,
           e, stride,
           count);

// Prints "[260, 200, 180, 200, 260]".
printf("[%g, %g, %g, %g, %g]\n", e[0], e[1], e[2], e[3], e[4]);
```

## Parameters

- `__A`: The input vector `A` in `E = (A * B) + (C * D)`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input vector `B` in `E = (A * B) + (C * D)`.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C`: The input vector `C` in `E = (A * B) + (C * D)`.
- `__IC`: The distance between the elements in the input vector `C`.
- `__D`: The input vector `D` in `E = (A * B) + (C * D)`.
- `__ID`: The distance between the elements in the input vector `D`.
- `__E`: The output vector `E` in `E = (A * B) + (C * D)`.
- `__IE`: The distance between the elements in the output vector `E`.
- `__N`: The number of elements that the function processes.

## See Also

### Quaternary multiply-multiply-add operations
- [vDSP_vmma](./vdsp_vmma.md)
  Calculates the single-precision element-wise sum of the products of two pairs of vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmmad)*