# vDSP_vsortiD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs an in-place sort of the indices into a double-precision vector.

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
extern void vDSP_vsortiD(const double *__C, vDSP_Length *__I, vDSP_Length *__Temporary, vDSP_Length __N, int __Order);
```

## Discussion

The following code sorts the indices into an array in ascending order, followed by decending order:

**Swift**:

```swift
let values: [Double] = [4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0]

let n = vDSP_Length(values.count)

var indices = ( 0 ..< n ).map { $0 }

vDSP_vsortiD(values, &indices, nil, n, 1)

// Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
print(indices.map { values[Int($0)] })

vDSP_vsortiD(values, &indices, nil, n, -1)

// Prints "[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]".
print(indices.map { values[Int($0)] })
```

**Objective-C**:

```objc
double values[] = {4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0};
vDSP_Length n = 10;

vDSP_Length indices[10];
for (vDSP_Length i = 0; i < n; i++) indices[i] = i;

vDSP_vsortiD(values, indices, NULL, n, 1);

// Prints "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
      values[indices[0]], values[indices[1]], values[indices[2]],
      values[indices[3]], values[indices[4]], values[indices[5]],
      values[indices[6]], values[indices[7]], values[indices[8]],
      values[indices[9]]);

for (vDSP_Length i = 0; i < n; i++) indices[i] = i;

vDSP_vsortiD(values, indices, NULL, n, -1);

// Prints "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
      values[indices[0]], values[indices[1]], values[indices[2]],
      values[indices[3]], values[indices[4]], values[indices[5]],
      values[indices[6]], values[indices[7]], values[indices[8]],
      values[indices[9]]);
```

Note that this function doesn’t provide a stable sort. So, if the function compares two elements as equal, it may place them in any order within the sorted array.

## Parameters

- `__C`: The input vector that defines the source values.
- `__I`: The input vector that defines the indices. On input, the values `0 ..< n`. On output, the sorted indices.
- `__Temporary`: A temporary vector that this function doesn’t use. Pass `nil`.
- `__N`: The number of elements in the vector.
- `__Order`: A value that specifies the sort order. Pass `1` to specify ascending order, or `-1` for descending order.

## See Also

### Vector sorting functions
- [vDSP_vsort](./vdsp_vsort.md)
  Performs an in-place sort of a single-precision vector.
- [vDSP_vsortD](./vdsp_vsortd.md)
  Performs an in-place sort of a double-precision vector.
- [vDSP_vsorti](./vdsp_vsorti.md)
  Performs an in-place sort of the indices into a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsortid)*