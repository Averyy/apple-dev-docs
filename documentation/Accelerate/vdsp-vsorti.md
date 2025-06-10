# vDSP_vsorti

**Framework**: Accelerate  
**Kind**: func

Performs an in-place sort of the indices into a single-precision vector.

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
extern void vDSP_vsorti(const float * __C, vDSP_Length * __I, vDSP_Length * __Temporary, vDSP_Length __N, int __Order);
```

#### Discussion

The following code sorts the indices into an array in ascending order, followed by decending order:

```swift
    let values: [Float] = [4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0]
    
    let n = vDSP_Length(values.count)
    
    var indices = ( 0 ..< n ).map { $0 }
    
    vDSP_vsorti(values, &indices, nil, n, 1)
    
    // Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
    print(indices.map { values[Int($0)] })
    
    vDSP_vsorti(values, &indices, nil, n, -1)
    
    // Prints "[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]".
    print(indices.map { values[Int($0)] })
```

## Parameters

- `__C`: The input vector that defines the source values.
- `__I`: The input vector that defines the indices. On input, the values  . On output, the sorted indices.
- `__Temporary`: A temporary vector that this function doesn’t use. Pass  .
- `__N`: The number of elements in the vector.
- `__Order`: A value that specifies the sort order. Pass   to specify ascending order, or   for descending order.

## See Also

- [vDSP_vsort](vdsp_vsort.md)
  Performs an in-place sort of a single-precision vector.
- [vDSP_vsortD](vdsp_vsortd.md)
  Performs an in-place sort of a double-precision vector.
- [vDSP_vsortiD](vdsp_vsortid.md)
  Performs an in-place sort of the indices into a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsorti)*