# radius

**Framework**: SceneKit  
**Kind**: property

The radius of the wheel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var radius: CGFloat { get set }
```

#### Discussion

When you create a wheel from a node, its default radius is half of the largest dimension of the node’s bounding box. (A wheel is always circular, even if the content of the node representing it is not.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/radius)*