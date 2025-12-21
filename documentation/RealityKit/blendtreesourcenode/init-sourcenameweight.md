# init(source:name:weight:)

**Framework**: RealityKit  
**Kind**: init

Creates a node that defines an animation within a tree of other blend nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(source: any AnimationDefinition, name: String = "", weight: BlendWeight = .value(1.0))
```

## Parameters

- `source`: The blend node’s animation.
- `name`: A textual name for the blend node.
- `weight`: A normalized percentage that designates how much effect this   node has compared to peer nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreesourcenode/init(source:name:weight:))*