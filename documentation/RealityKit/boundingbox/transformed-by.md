# transformed(by:)

**Framework**: RealityKit  
**Kind**: method

Transforms the bounding box and finds the bounds of the result.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
func transformed(by transform: float4x4) -> BoundingBox
```

#### Return Value

The bounds of the transformed box.

## Parameters

- `transform`: The transform to apply to the box.

## See Also

- [func transform(by: float4x4)](boundingbox/transform(by:).md)
  Transforms the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/transformed(by:))*