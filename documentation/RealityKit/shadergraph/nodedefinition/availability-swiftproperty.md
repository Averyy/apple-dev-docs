# availability

**Framework**: RealityKit  
**Kind**: property

The availability of this node definition on each platform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var availability: [ShaderGraph.NodeDefinition.Platform : ShaderGraph.NodeDefinition.Availability] { get }
```

#### Discussion

Prefer [`isAvailable(on:version:)`](shadergraph/nodedefinition/isavailable(on:version:).md) for point-in-time availability checks. Use this property when you need the full version range — for example, to display availability annotations in a node library UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/availability-swift.property)*