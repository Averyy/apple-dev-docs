# SPProjectiveTransform3DAlmostEqualToTransform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two transforms are equal within a default tolerance.

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
static bool SPProjectiveTransform3DAlmostEqualToTransform(SPProjectiveTransform3D t1, SPProjectiveTransform3D t2);
```

## Return Value

`true` if the two transforms are nearly equal to each other. The absolute default tolerance is

## Overview

The default absolute tolerance is [`ulpOfOne`](../Swift/floatingpoint/ulpofone-3j2pj.md) in Swift or `DBL_EPSILON` in Objective-C.

## Parameters

- `t1`: The first projective transform to compare.
- `t2`: The second projective transform to compare.

## See Also

### Comparing values
- [SPProjectiveTransform3DAlmostEqualToTransform](./spprojectivetransform3dalmostequaltotransform-33crc.md)
  Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dalmostequaltotransform-5qqyc)*