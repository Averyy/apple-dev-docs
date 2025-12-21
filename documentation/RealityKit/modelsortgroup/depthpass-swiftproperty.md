# depthPass

**Framework**: RealityKit  
**Kind**: property

A depth pass that controls when the renderer draws the depth of model entities in the group relative to their color.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var depthPass: ModelSortGroup.DepthPass? { get }
```

#### Discussion

You can tell the renderer to draw the depth and color together by setting the value to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelsortgroup/depthpass-swift.property)*