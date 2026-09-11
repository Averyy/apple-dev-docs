# availability

**Framework**: RealityKit  
**Kind**: property

The availability of this node definition on each platform.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var availability: [ShaderGraph.NodeDefinition.Platform : ShaderGraph.NodeDefinition.Availability] { get }
```

#### Discussion

Prefer [`isAvailable(on:version:)`](shadergraph/nodedefinition/isavailable(on:version:).md) for point-in-time availability checks. Use this property when you need the full version range — for example, to display availability annotations in a node library UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/availability-swift.property)*