# vDSP_vsortD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs an in-place sort of a double-precision vector.

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
extern void vDSP_vsortD(double *__C, vDSP_Length __N, int __Order);
```

#### Discussion

The following code sorts an array in ascending order, followed by decending order:

**Swift**:

```swift
var values: [Double] = [4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0]

let n = vDSP_Length(values.count)

vDSP_vsortD(&values, n, 1)

// Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
print(values)

vDSP_vsortD(&values, n, -1)

// Prints "[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]".
print(values)
```

**Objective-C**:

```objc
double values[] = {4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0};
vDSP_Length n = 10;

vDSP_vsortD(values, n, 1);

// Prints "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
      values[0], values[1], values[2], values[3], values[4],
      values[5], values[6], values[7], values[8], values[9]);

vDSP_vsortD(values, n, -1);

// Prints "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
      values[0], values[1], values[2], values[3], values[4],
      values[5], values[6], values[7], values[8], values[9]);
```

## Parameters

- `__C`: The vector that the function sorts in-place.
- `__N`: The number of elements in the vector.
- `__Order`: A value that specifies the sort order. Pass `1` to specify ascending order, or `-1` for descending order.

## See Also

### Vector sorting functions
- [vDSP_vsort](./vdsp_vsort.md)
  Performs an in-place sort of a single-precision vector.
- [vDSP_vsorti](./vdsp_vsorti.md)
  Performs an in-place sort of the indices into a single-precision vector.
- [vDSP_vsortiD](./vdsp_vsortid.md)
  Performs an in-place sort of the indices into a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsortd)*