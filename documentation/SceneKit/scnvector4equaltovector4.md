# SCNVector4EqualToVector4(_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a Boolean value that indicates whether the corresponding components of two vectors are equal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SCNVector4EqualToVector4(_ a: SCNVector4, _ b: SCNVector4) -> Bool
```

#### Return Value

True if each component of `a` is exactly equal to `b`.

#### Discussion

This function performs a numeric (not bitwise) comparison of each pair of component values.

## Parameters

- `a`: The first vector.
- `b`: The second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector4equaltovector4(_:_:))*