# vDSP_vmsa

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision element-wise sum of the product of two vectors, and a scalar value, using the specified stride.

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
extern void vDSP_vmsa(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, const float *__C, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Mentions

- [Using vDSP for vector-based arithmetic](./using-vdsp-for-vector-based-arithmetic.md)

## Discussion

This function calculates the element-wise product of vectors `A` and `B`, adds scalar value `C` to the product, and writes the result to vector `D`, as follows:

```c
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B[n] + C;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row represents the operation that multiplies A and B, with three boxes, as well as the input scalar C with one box. The third row represents the addition operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.   ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4387443@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = 1
let count = 5

let a: [Float] = [ 1,  2,  3,  4,  5]
let b: [Float] = [10, 20, 30, 40, 50]
let c: Float = 5

let d = [Float](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vmsa(a, stride,
              b, stride,
              [c],
              buffer.baseAddress!, stride,
              vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[15.0, 45.0, 95.0, 165.0, 255.0]s".
print(d)
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;
vDSP_Length count = 5;

float a[] = { 1,  2,  3,  4,  5};
float b[] = {10, 20, 30, 40, 50};
float c = 5;

float d[5];

vDSP_vmsa(a, stride,
          b, stride,
          &c,
          d, stride,
          count);

// Prints "[15, 45, 95, 165, 255]".
printf("[%g, %g, %g, %g, %g]\n", d[0], d[1], d[2], d[3], d[4]);
```

## Parameters

- `__A`: The input vector `A` in `D = (A * B) + C`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input vector `B` in `D = (A * B) + C`.
- `__IB`: The distance between the elements in the input vector `B`.
- `__C`: The input scalar value `C` in `D = (A * B) + C`.
- `__D`: The output vector `D` in `D = (A * B) + C`.
- `__ID`: The distance between the elements in the output vector `D`.
- `__N`: The number of elements that the function processes.

## See Also

### Vector-vector-scalar multiply-add operations
- [vDSP_vmsaD](./vdsp_vmsad.md)
  Calculates the double-precision element-wise sum of the product of two vectors, and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmsa)*