# vDSP_vsort

**Framework**: Accelerate  
**Kind**: func

Performs an in-place sort of a single-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vsort(float * __C, vDSP_Length __N, int __Order);
```

#### Discussion

The following code sorts an array in ascending order, followed by decending order:

```swift
    var values: [Float] = [4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0]

    let n = vDSP_Length(values.count)
    
    vDSP_vsort(&values, n, 1)

    // Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
    print(values)

    vDSP_vsort(&values, n, -1)

    // Prints "[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]".
    print(values)
```

## Parameters

- `__C`: The vector that the function sorts in-place.
- `__N`: The number of elements in the vector.
- `__Order`: A value that specifies the sort order. Pass   to specify ascending order, or   for descending order.

## See Also

- [vDSP_vsortD](vdsp_vsortd.md)
  Performs an in-place sort of a double-precision vector.
- [vDSP_vsorti](vdsp_vsorti.md)
  Performs an in-place sort of the indices into a single-precision vector.
- [vDSP_vsortiD](vdsp_vsortid.md)
  Performs an in-place sort of the indices into a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsort)*