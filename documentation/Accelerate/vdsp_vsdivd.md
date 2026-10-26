# vDSP_vsdivD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise division of a vector and a scalar value, using the specified stride.

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
extern void vDSP_vsdivD(const double *__A, vDSP_Stride __IA, const double *__B, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise division of vector `A` and scalar value `B`, and writes the result to vector `C`, as follows:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B;
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337201@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = 1
    let count = 5
    
    let a: [Double] = [1, 2, 3, 4, 5]
    let b: Double = 10
    
    let c = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsdivD(a, stride,
                    [b],
                    buffer.baseAddress!, stride,
                    vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[0.1, 0.2, 0.3, 0.4, 0.5]".
    print(c)
```

**Objective-C**:

```objc
int stride = 1;
int count = 5;

double a[5] = {1, 2, 3, 4, 5};
double b = 10;
double c[5] = {0, 0, 0, 0, 0};

vDSP_vsdivD(a, stride,
            &b,
            c, stride,
            (vDSP_Length)count);

// Prints "[0.1, 0.2, 0.3, 0.4, 0.5]".
printf("[%g, %g, %g, %g, %g]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__A`: The input vector, `A`.
- `__IA`: The distance between the elements in the input vector.
- `__B`: The input scalar, `B`.
- `__C`: The output vector, `C`.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Vector-scalar division operations
- [vDSP_vsdivi](./vdsp_vsdivi.md)
  Calculates the integer element-wise division of a vector and a scalar value, using the specified stride.
- [vDSP_vsdiv](./vdsp_vsdiv.md)
  Calculates the single-precision element-wise division of a vector and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsdivd)*