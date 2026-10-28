# init(radius:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a sphere geometry with the specified radius.

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
convenience init(radius: CGFloat)
```

```objc
+ (instancetype) sphereWithRadius:(CGFloat) radius;
```

## Return Value

A new sphere geometry.

## Discussion

The sphere is centered in its local coordinate system. For example, if you create a sphere whose radius is `5.0`, it extends from `-5.0` to `5.0` along each of the the x, y, and z-axes.

## Parameters

- `radius`: The radius of the sphere in its local coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsphere/init(radius:))*