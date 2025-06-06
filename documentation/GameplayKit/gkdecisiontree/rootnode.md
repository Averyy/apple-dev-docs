# rootNode

**Framework**: GameplayKit  
**Kind**: property

The decision node at the root of the decision tree, representing the first attribute to test.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var rootNode: GKDecisionNode? { get }
```

#### Discussion

To build a manually defined tree, use [`GKDecisionNode`](gkdecisionnode.md) methods on that object to create branches leading to child nodes that represent additional attributes to test or final actions.

## See Also

- [init(attribute: any NSObjectProtocol)](gkdecisiontree/init(attribute:).md)
  Creates a decision tree starting with the specified initial attribute to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/rootnode)*