# vDSP_vclr

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Populates a single-precision vector with zeros.

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
extern void vDSP_vclr(float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The [`vDSP_vclr`](./vdsp_vclr.md) and [`vDSP_vclrD`](./vdsp_vclrd.md) functions populate a vector with zeros.

The following code shows how to clear the array c, setting the value of each element to zero:

**Swift**:

```swift
    let n = vDSP_Length(10)
    let stride = vDSP_Stride(1)

    var c = [Float](repeating: .nan,
                    count: Int(n))

    vDSP_vclr(&c,
              stride,
              n)

    // Prints "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]".
    print(c)
```

**Objective-C**:

```objc
    vDSP_Length n = 10;
    vDSP_Stride stride = 1;

    float c[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    vDSP_vclr(c, stride, n);

    // Prints "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]".
    printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
          c[0], c[1], c[2], c[3], c[4],
          c[5], c[6], c[7], c[8], c[9]);
```

## Parameters

- `__C`: Single-precision real output vector.
- `__IC`: Address stride for `C`.
- `__N`: The number of elements to process.

## See Also

### Clearing Vectors
- [vDSP_vclrD](./vdsp_vclrd.md)
  Populates a double-precision vector with zeros.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vclr)*