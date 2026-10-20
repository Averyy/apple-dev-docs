# weight

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A normalized percentage that designates how much effect this node has relative to peer nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var weight: BlendWeight { get set }
```

#### Discussion

The value of this property relates to the node’s peers in a [`sources`](../blendtreeblendnode/sources.md) array. The sum of all node weights in a given [`sources`](../blendtreeblendnode/sources.md) array needs to equal `1.0`.

## See Also

### Configuring the blend tree node
- [var name: String](./name.md)
  A textual name for the blend node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreenode/weight)*