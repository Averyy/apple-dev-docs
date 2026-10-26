# vDSP_zvsma

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision element-wise addition of the product of a complex vector and a complex scalar value, and a complex vector, using the specified stride.

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
extern void vDSP_zvsma(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__B, const DSPSplitComplex *__C, vDSP_Stride __IC, const DSPSplitComplex *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, adds vector `C` to the product, and writes the result to vector `D`, as follows:

```c
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B + C[n];
```

![A diagram showing the operation of the function. There are four rows. The top row represents the input vector, A, with three boxes, and the scalar value B, with one box. The second row represents the operation that multiplies A and B, with three boxes, as well as the input vector C with three boxes. The third row represents the addition operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4387632@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
let stride = 1
let count = 5

let a: [Float] = [ 1,  2,  3,  4,  5]
let b: Float = 10
let c: [Float] = [ 5,  4,  3,  2,  1]

let d = [Float](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vsma(a, stride,
              [b],
              c, stride,
              buffer.baseAddress!, stride,
              vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[15.0, 24.0, 33.0, 42.0, 51.0]".
print(d)
```

**Objective-C**:

```objc
float a[5] = {1, 2, 3, 4, 5};
float b = 10;
float c[5] = {5, 4, 3, 2, 1};
float d[5];

vDSP_vsma(a, 1, &b, c, 1, d, 1, 5);

// Prints "[15, 24, 33, 42, 51]".
printf("[%g, %g, %g, %g, %g]\n", d[0], d[1], d[2], d[3], d[4]);
```

## Parameters

- `__A`: The input vector `A` in `D = (A * B) + C`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input scalar value `B` in `D = (A * B) + C`.
- `__C`: The input vector `C` in `D = (A * B) + C`.
- `__IC`: The distance between the elements in the input vector `C`.
- `__D`: The output vector `D` in `D = (A * B) + C`.
- `__ID`: The distance between the elements in the output vector `D`.
- `__N`: The number of elements that the function processes.

## See Also

### Ternary Multiply-Add Operations
- [vDSP_zvma](./vdsp_zvma.md)
  Adds a single-precision complex vector to the product of two single-precision complex vectors.
- [vDSP_zvmaD](./vdsp_zvmad.md)
  Adds a double-precision complex vector to the product of two double-precision complex vectors.
- [vDSP_zvsmaD](./vdsp_zvsmad.md)
  Calculates the double-precision element-wise addition of the product of a complex vector and a complex scalar value, and a complex vector, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvsma)*