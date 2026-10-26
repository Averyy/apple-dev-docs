# vDSP_vrvrsD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs an in-place reversal of a double-precision vector.

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
extern void vDSP_vrvrsD(double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code reverses the elements in the array `values`:

**Swift**:

```swift
var values: [Double] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

let stride = 1
let n = vDSP_Length(values.count)

vDSP_vrvrsD(&values, stride,
            n)

// Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
print(values)
```

**Objective-C**:

```objc
double values[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

vDSP_vrvrsD(values, 1, 10);

// Prints "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
      values[0], values[1], values[2], values[3], values[4],
      values[5], values[6], values[7], values[8], values[9]);
```

## Parameters

- `__C`: The vector that the function reverses in-place.
- `__IC`: The distance between the elements in the vector.
- `__N`: The number of elements in the vector.

## See Also

### Vector reversing functions
- [vDSP_vrvrs](./vdsp_vrvrs.md)
  Performs an in-place reversal of a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrvrsd)*