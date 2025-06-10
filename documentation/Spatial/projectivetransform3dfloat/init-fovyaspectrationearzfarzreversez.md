# init(fovY:aspectRatio:nearZ:farZ:reverseZ:)

**Framework**: Spatial  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(fovY: Angle2DFloat, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool)
```

#### Return Value

A projective transform with right-hand side perspective.

## Parameters

- `fovY`: The field of view angle on the @p y axis.
- `aspectRatio`: The aspect ratio.
- `nearZ`: The near @p z .
- `farZ`: The far @p z .
- `reverseZ`: A Boolean value that specifies whether the matrix should use reverse z.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/init(fovy:aspectratio:nearz:farz:reversez:))*