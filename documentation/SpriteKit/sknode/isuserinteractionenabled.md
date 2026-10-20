# isUserInteractionEnabled

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the node receives touch events.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var isUserInteractionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isUserInteractionEnabled) BOOL userInteractionEnabled;
```

## Mentions

- [Controlling User Interaction on Nodes](../controlling-user-interaction-on-nodes.md)
- [Understanding Hit-Testing](../understanding-hit-testing.md)

#### Discussion

The default value is [`false`](../../Swift/false.md).

> ❗ **Important**:  In addition to setting `isUserInteractionEnabled` to `true`, you must subclass the node and define event callbacks in order to respond to user input.

## See Also

### Handling User Input
- [Controlling User Interaction on Nodes](../controlling-user-interaction-on-nodes.md)
  Enable your node to respond to user input, like touches or mouse clicks.
- [var focusBehavior: SKNodeFocusBehavior](./focusbehavior.md)
  The focus behavior for a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/isuserinteractionenabled)*