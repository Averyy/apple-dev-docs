# GKDecisionNode

**Framework**: GameplayKit  
**Kind**: class  
**Role**: Class

A node for use in manually creating decision trees, representing a specific question and possible answers, or an action that follows from answering other questions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKDecisionNode
```

```objc
@interface GKDecisionNode : NSObject
```

## Overview

A [`GKDecisionNode`](./gkdecisionnode.md) instance represents an element in a decision tree (a [`GKDecisionTree`](./gkdecisiontree.md) object). Decision trees contain two kinds of nodes. Some nodes, including the tree’s root node, represent individual decisions to be made (also called a question or *attribute*) and reference child nodes for each possible outcome of (or *branch* from) that decision. Each branch can lead to another question node, or to a leaf node—nodes that have no branches represent a final outcome (or *action*) to result from the tree’s decision-making process. After creating a decision tree from a set of nodes, you can present the tree with a set of inputs (values for attributes, or answers to questions) and the tree provides a final action that follows from the branches corresponding to each attribute.

There are two ways to create a decision tree. You use the [`GKDecisionNode`](./gkdecisionnode.md) class directly only when you want to define an entire decision tree manually—that is, to specify each question, the possible branches from each question, and the possible final actions. To create such a decision tree, start with the [`GKDecisionTree`](./gkdecisiontree.md)  [`init(attribute:)`](./gkdecisiontree/init%28attribute%29.md) initializer, then use the methods listed in Creating Child Nodes for Decision Branches to add branches to the tree.

To instead automatically learn a decision tree given a set of questions and example answers, use the [`GKDecisionTree`](./gkdecisiontree.md)  [`init(examples:actions:attributes:)`](./gkdecisiontree/init%28examples,actions,attributes%29.md) method.

## Topics

### Creating Child Nodes for Decision Branches
- [func createBranch(value: NSNumber, attribute: any NSObjectProtocol) -> Self](./gkdecisionnode/createbranch%28value,attribute%29.md)
  Creates a child node that the decision tree should use when the current node’s attribute has the specified value.
- [func createBranch(predicate: NSPredicate, attribute: any NSObjectProtocol) -> Self](./gkdecisionnode/createbranch%28predicate,attribute%29.md)
  Creates a child node that the decision tree should use when the current node’s attribute satisfies the specified predicate.
- [func createBranch(weight: Int, attribute: any NSObjectProtocol) -> Self](./gkdecisionnode/createbranch%28weight,attribute%29.md)
  Creates a child node that the decision tree should use as the result of a random choice, biased by the specified weight.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Decision Trees
- [class GKDecisionTree](./gkdecisiontree.md)
  A data structure that models a set of specific questions, their possible answers, and the actions that follow from a series of answers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode)*