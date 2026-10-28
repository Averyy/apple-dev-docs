# vDSP_vaddi

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Adds two integer vectors.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vaddi(const int *__A, vDSP_Stride __IA, const int *__B, vDSP_Stride __IB, int *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function calculates the sums of the first `N` elements of `A` and `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_vaddi function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110581@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B[n];
```

The following code shows an example of using [`vDSP_vaddi`](./vdsp_vaddi.md):

**Swift**:

```swift
    let stride = vDSP_Stride(1)

    let a: [Int32] = [10, 20, 30, 40, 50]
    let b: [Int32] = [ 1,  2,  3,  4,  5]

    let n = vDSP_Length(a.count)

    var c = [Int32](repeating: 0,
                    count: a.count)

    vDSP_vaddi(a, stride,
               b, stride,
               &c, stride,
               n)

    // Prints "[11, 22, 33, 44, 55]".
    print(c)
```

**Objective-C**:

```objc
    vDSP_Stride stride = 1;

    int a[] = {10, 20, 30, 40, 50};
    int b[] = { 1,  2,  3,  4,  5};
    vDSP_Length n = 5;
    int c[5] = {0, 0, 0, 0, 0};

    vDSP_vaddi(a, stride,
               b, stride,
               c, stride,
               n);

    // Prints "[11, 22, 33, 44, 55]".
    printf("[%d, %d, %d, %d, %d]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__A`: Integer input vector.
- `__IA`: Stride for `A`.
- `__B`: Integer input vector
- `__IB`: Stride for `B`.
- `__C`: Integer result vector.
- `__IC`: Stride for `C`.
- `__N`: Number of elements to process in the input and output vectors.

## See Also

### Vector-to-Vector Integer Arithmetic
- [vDSP_veqvi](./vdsp_veqvi.md)
  Calculates bitwise logical equivalence of two integer vectors.
- [vDSP_vdivi](./vdsp_vdivi.md)
  Divides two integer vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vaddi)*