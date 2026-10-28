# SPSize3DUnion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the smallest size that contains two sizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPSize3D SPSize3DUnion(SPSize3D size, SPSize3D other);
```

## Return Value

A new size that is the union of two sizes.

## Parameters

- `size`: The size object to compare.
- `other`: The size objectd that the function compares against.

## See Also

### Creating derived 3D sizes
- [SPSize3DIntersection](./spsize3dintersection.md)
  Returns the intersection of two sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dunion)*