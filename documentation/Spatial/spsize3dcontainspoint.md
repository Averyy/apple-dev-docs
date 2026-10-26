# SPSize3DContainsPoint

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the size contains the specified point.

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
static bool SPSize3DContainsPoint(SPSize3D size, SPPoint3D other);
```

#### Return Value

A Boolean value that indicates whether the size contains the specified point.

## Parameters

- `size`: The size object to compare.
- `other`: The point that the function compares against.

## See Also

### Checking characteristics
- [SPSize3DContainsAnyPoint](./spsize3dcontainsanypoint.md)
  Returns a Boolean value that indicates whether the size contains the specified point.
- [SPSize3DContainsSize](./spsize3dcontainssize.md)
  Returns a Boolean value that indicates whether the size contains the specified size.
- [SPSize3DIsValid](./spsize3disvalid.md)
  A Boolean value that indicates whether the size represents a valid value.
- [SPSize3DIsFinite](./spsize3disfinite.md)
- [SPSize3DIsNaN](./spsize3disnan.md)
- [SPSize3DIsZero](./spsize3diszero.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dcontainspoint)*