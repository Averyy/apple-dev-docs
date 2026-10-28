# init(fovY:aspectRatio:nearZ:farZ:reverseZ:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(fovY: Angle2DFloat, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool)
```

```c
static SPProjectiveTransform3DFloat SPProjectiveTransform3DFloatMakeWithRightHandPerspective(SPAngleFloat fovY, float aspectRatio, float nearZ, float farZ, bool reverseZ);
```

## Return Value

A projective transform with right-hand side perspective.

## Discussion

Returns a projective transform with right-hand side perspective.

## Parameters

- `fovY`: The field of view angle on the @p y axis.
- `aspectRatio`: The aspect ratio.
- `nearZ`: The near @p z .
- `farZ`: The far @p z .
- `reverseZ`: A Boolean value that specifies whether the matrix should use reverse z.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/init(fovy:aspectratio:nearz:farz:reversez:))*