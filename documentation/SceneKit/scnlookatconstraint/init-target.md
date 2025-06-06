# init(target:)

**Framework**: SceneKit  
**Kind**: init

Creates a look-at constraint for a specified target node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init(target: SCNNode?)
```

#### Return Value

A constraint object.

#### Discussion

To attach constraints to an [`SCNNode`](scnnode.md) object, use its [`constraints`](scnnode/constraints.md) property.

## Parameters

- `target`: The node that constrained nodes will be reoriented to point toward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/init(target:))*