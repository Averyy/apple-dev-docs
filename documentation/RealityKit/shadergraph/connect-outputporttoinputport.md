# connect(_:outputPort:to:inputPort:)

**Framework**: RealityKit  
**Kind**: method

Connect a node with a given output, to a node with a given input. If outputPort is nil, the first output on outputNode is used.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func connect(_ outputNode: ShaderGraph.Node, outputPort: String? = nil, to inputNode: ShaderGraph.Node, inputPort: String) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/connect(_:outputport:to:inputport:))*