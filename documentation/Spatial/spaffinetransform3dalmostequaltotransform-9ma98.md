# SPAffineTransform3DAlmostEqualToTransform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

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
static bool SPAffineTransform3DAlmostEqualToTransform(SPAffineTransform3D t1, SPAffineTransform3D t2, double tolerance);
```

## Return Value

A Boolean value that indicates whether the two rotations are equal within the default absolute tolerance.

## Overview

The default absolute tolerance is [`ulpOfOne`](../Swift/floatingpoint/ulpofone-3j2pj.md) in Swift or `DBL_EPSILON` in Objective-C.

## Parameters

- `t1`: The first rotation.
- `t2`: The second rotation.
- `tolerance`: How close the two rotations must be to be considered “almost equal”.

## See Also

### Comparing values
- [SPAffineTransform3DAlmostEqualToTransform](./spaffinetransform3dalmostequaltotransform-16ryg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dalmostequaltotransform-9ma98)*