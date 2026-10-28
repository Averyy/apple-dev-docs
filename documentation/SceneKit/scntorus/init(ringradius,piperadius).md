# init(ringRadius:pipeRadius:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a torus geometry with the specified ring radius and pipe radius.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
convenience init(ringRadius: CGFloat, pipeRadius: CGFloat)
```

```objc
+ (instancetype) torusWithRingRadius:(CGFloat) ringRadius pipeRadius:(CGFloat) pipeRadius;
```

## Return Value

A new torus geometry.

## Discussion

The torus is centered in its local coordinate system. For example, if you create a torus whose ring radius is `5.0` and pipe radius is `1.0`, it extends from `-6.0` to `6.0` (with a hole through the center from `-4.0` to `4.0`) in the x- and z-axes and from `-1.0` to `1.0` in the y-axis.

## Parameters

- `ringRadius`: The major radius of the torus, defining its circular ring in the x- and z-axis dimensions of its local coordinate space.
- `pipeRadius`: The minor radius of the torus, defining the pipe that encircles the ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/init(ringradius:piperadius:))*