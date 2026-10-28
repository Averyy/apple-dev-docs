# viewMatrixForOrientation:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns a transform matrix for converting from world space to camera space.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0

## Declaration

```objc
- (simd_float4x4) viewMatrixForOrientation:(UIInterfaceOrientation) orientation;
```

## Return Value

A view matrix appropriate for the camera with the specified orientation.

## Discussion

This method has no effect on ARKit. Instead, this method uses the orientation parameter and the camera’s state to construct a view matrix for your own rendering code.

The view matrix can be used to transform geometry from world space into camera space for a given orientation.

## Parameters

- `orientation`: The orientation in which the camera image is to be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/viewmatrixfororientation:)*