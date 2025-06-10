# isUserInteractionEnabled

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the node receives touch events.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
var isUserInteractionEnabled: Bool { get set }
```

## Mentions

- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)
- [Understanding Hit-Testing](understanding-hit-testing.md)

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

> ❗ **Important**:  In addition to setting `isUserInteractionEnabled` to `true`, you must subclass the node and define event callbacks in order to respond to user input.

## See Also

- [Controlling User Interaction on Nodes](controlling-user-interaction-on-nodes.md)
  Enable your node to respond to user input, like touches or mouse clicks.
- [var focusBehavior: SKNodeFocusBehavior](sknode/focusbehavior.md)
  The focus behavior for a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/isuserinteractionenabled)*