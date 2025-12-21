# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Accessor for reading a blend shape weights data in the set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
subscript(blendShapeName: String) -> BlendShapeWeightsSet.Element? { get }
```

#### Return Value

Blend shape weights data associated with the given name owned by this set, or nil if not found.

## Parameters

- `blendShapeName`: The name of the blend shape to be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightsset/subscript(_:))*