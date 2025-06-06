# isPaused

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether to run actions and animations attached to the node and its child nodes.

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
var isPaused: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), specifying that SceneKit should continuously update the node’s contents. Pausing a node pauses any running animations or actions. This property applies to the actions and animations attached to the node itself and those attached to any of its child or descendant nodes.

## See Also

- [var presentation: SCNNode](scnnode/presentation.md)
  A node object representing the state of the node as it currently appears onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/ispaused)*