# init(attribute:)

**Framework**: GameplayKit  
**Kind**: init

Creates a decision tree starting with the specified initial attribute to test.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(attribute: any NSObjectProtocol)
```

#### Return Value

A new decision tree.

#### Discussion

The decision tree returned by this initializer is incomplete. To build a manually defined tree, use the [`rootNode`](gkdecisiontree/rootnode.md) property to access the node corresponding to the initial attribute, and use [`GKDecisionNode`](gkdecisionnode.md) methods on that object to create branches leading to child nodes that represent additional attributes to test or final actions.

## Parameters

- `attribute`: The first attribute to test (or question to answer) when evaluating the tree.

## See Also

- [var rootNode: GKDecisionNode?](gkdecisiontree/rootnode.md)
  The decision node at the root of the decision tree, representing the first attribute to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/init(attribute:))*