# SCNVector3EqualToVector3(_:_:)

**Framework**: SceneKit  
**Kind**: func

Returns a Boolean value that indicates whether the corresponding components of two vectors are equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func SCNVector3EqualToVector3(_ a: SCNVector3, _ b: SCNVector3) -> Bool
```

#### Return Value

True if each component of `a` is exactly equal to `b`.

#### Discussion

This function performs a numeric (not bitwise) comparison of each pair of component values.

## Parameters

- `a`: The first vector.
- `b`: The second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector3equaltovector3(_:_:))*