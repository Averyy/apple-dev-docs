# vDSP_vdivi

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Divides two integer vectors.

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
extern void vDSP_vdivi(const int *__B, vDSP_Stride __IB, const int *__A, vDSP_Stride __IA, int *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the first `N` elements of `A` divided by the corresponding element in `B`, writing the result to `C`:

![A diagram showing the operation of the vDSP_vdivi function. There are three rows. The top row represents the first input, vector A. The second row represents the second input, vector B. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the output vector indicating the relationships between the inputs and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3110580@2x.png)

The operation is:

```c
 for (n = 0; n < N; ++n)
    C[n] = A[n] / B[n];
```

The following code shows an example of using [`vDSP_vdiv`](./vdsp_vdiv.md):

**Swift**:

```swift
let stride = vDSP_Stride(1)

let a: [Int32] = [10, 20, 30, 40, 50]
let b: [Int32] = [ 1,  2,  3,  4,  5]

let n = vDSP_Length(a.count)

var c = [Int32](repeating: 0,
                count: a.count)

vDSP_vdivi(b, stride,
           a, stride,
           &c, stride,
           n)

// Operand-order trap: `vDSP_vdivi` divides the second input by the first, so passing `(B, A)` computes `C = A / B`.
// Prints "[10, 10, 10, 10, 10]".
print(c)
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;

int a[5] = {10, 20, 30, 40, 50};
int b[5] = {1, 2, 3, 4, 5};

vDSP_Length n = 5;

int c[5] = {0};

vDSP_vdivi(b, stride,
           a, stride,
           c, stride,
           n);

// Operand-order trap: `vDSP_vdivi` divides the second input by the first, so passing `(B, A)` computes `C = A / B`.
// Prints "[10, 10, 10, 10, 10]".
printf("[%d, %d, %d, %d, %d]\n", c[0], c[1], c[2], c[3], c[4]);
```

## Parameters

- `__B`: Integer input vector. Note that `B` comes before `A`!
- `__IB`: Stride for `B`.
- `__A`: Integer input vector.
- `__IA`: Stride for `A`.
- `__C`: Integer output vector.
- `__IC`: Stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Vector-to-Vector Integer Arithmetic
- [vDSP_vaddi](./vdsp_vaddi.md)
  Adds two integer vectors.
- [vDSP_veqvi](./vdsp_veqvi.md)
  Calculates bitwise logical equivalence of two integer vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdivi)*