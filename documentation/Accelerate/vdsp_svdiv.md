# vDSP_svdiv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision element-wise division of a scalar value and a vector, using the specified stride.

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
extern void vDSP_svdiv(const float *__A, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Mentions

- [Using vDSP for vector-based arithmetic](./using-vdsp-for-vector-based-arithmetic.md)

#### Discussion

This function calculates the element-wise division of scalar value `A` and vector `B`, and writes the result to vector `C`, as follows:

```c
 for (n = 0; n < N; ++n)
    C[n] = A / B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the scalar value A with one box, and the input vector B with three boxes. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337225@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = 1
    let count = 5
    
    let a: Float = 100
    let b: [Float] = [1, 2, 3, 4, 5]
    
    let c = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_svdiv([a],
                   b, stride,
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[100.0, 50.0, 33.333, 25.0, 20.0]".
    print(c)
```

**Objective-C**:

```objc
int stride = 1;
int count = 5;

float a = 100;
float b[] = {1, 2, 3, 4, 5};
float c[5];

vDSP_svdiv(&a,
           b, stride,
           c, stride,
           (vDSP_Length)count);

// Prints "[100, 50, 33.333, 25, 20]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__A`: The input scalar, `A`.
- `__B`: The input vector, `B`.
- `__IB`: The distance between the elements in the input vector.
- `__C`: The output vector, `C`.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Scalar-vector division operations
- [vDSP_svdivD](./vdsp_svdivd.md)
  Calculates the double-precision element-wise division of a scalar value and a vector, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_svdiv)*