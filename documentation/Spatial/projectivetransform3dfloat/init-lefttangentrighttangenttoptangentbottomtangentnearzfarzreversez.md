# init(leftTangent:rightTangent:topTangent:bottomTangent:nearZ:farZ:reverseZ:)

**Framework**: Spatial  
**Kind**: init

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
init(leftTangent: Float, rightTangent: Float, topTangent: Float, bottomTangent: Float, nearZ: Float, farZ: Float, reverseZ: Bool)
```

#### Return Value

A projective transform from tangents for each side of its frustum.

#### Discussion

Returns a projective transform from tangents for each side of its frustum.

## Parameters

- `leftTangent`: The left tangent.
- `rightTangent`: The right tangent.
- `topTangent`: The top tangent.
- `bottomTangent`: Bottom left tangent.
- `nearZ`: The near @p z .
- `farZ`: The far @p z .
- `reverseZ`: A Boolean value that specifies whether the matrix should use reverse z.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/init(lefttangent:righttangent:toptangent:bottomtangent:nearz:farz:reversez:))*