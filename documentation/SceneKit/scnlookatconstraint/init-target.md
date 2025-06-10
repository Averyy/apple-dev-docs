# init(target:)

**Framework**: SceneKit  
**Kind**: init

Creates a look-at constraint for a specified target node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

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