# transformed(by:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Transforms the bounding box and finds the bounds of the result.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func transformed(by transform: float4x4) -> BoundingBox
```

#### Return Value

The bounds of the transformed box.

## Parameters

- `transform`: The transform to apply to the box.

## See Also

### Transforming a bounding box
- [func transform(by: float4x4)](./transform%28by%29.md)
  Transforms the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/transformed(by:))*