# vDSP_vsmsaD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a scalar value, using the specified stride.

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
extern void vDSP_vsmsaD(const double *__A, vDSP_Stride __IA, const double *__B, const double *__C, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, adds scalar value `C` to the product, and writes the result to vector `D`, as follows:

```c
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B + C;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The second row represents the operation that multiplies A and B, with three boxes, as well as the input vector C with three boxes. The third row represents the addition operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4387656@2x.png)

The following code shows an example of using this function:

**Swift**:

```swift
    let stride = 1
    let count = 5
    
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: Double = 10
    let c: Double = 5
    
    let d = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsmsaD(a, stride,
                   [b],
                   [c],
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[15.0, 25.0, 35.0, 45.0, 55.0]".
    print(d)
```

**Objective-C**:

```objc
int stride = 1;
int count = 5;

double a[5] = { 1,  2,  3,  4,  5};
double b = 10;
double c = 5;
double d[5] = {0, 0, 0, 0, 0};

vDSP_vsmsaD(a, stride,
            &b,
            &c,
            d, stride,
            (vDSP_Length)count);

// Prints "[15, 25, 35, 45, 55]".
printf("[%g, %g, %g, %g, %g]\n", d[0], d[1], d[2], d[3], d[4]);
```

## Parameters

- `__A`: The input vector `A` in `D = (A * B) + C`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__B`: The input scalar value `B` in `D = (A * B) + C`.
- `__C`: The input scalar value `B` in `D = (A * B) + C`.
- `__D`: The output vector `D` in `D = (A * B) + C`.
- `__ID`: The distance between the elements in the output vector `D`.
- `__N`: The number of elements that the function processes.

## See Also

### Vector-scalar-scalar multiply-add operations
- [vDSP_vsmsa](./vdsp_vsmsa.md)
  Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsmsad)*