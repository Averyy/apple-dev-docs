# createBranch(weight:attribute:)

**Framework**: GameplayKit  
**Kind**: method

Creates a child node that the decision tree should use as the result of a random choice, biased by the specified weight.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func createBranch(weight: Int, attribute: any NSObjectProtocol) -> Self
```

#### Return Value

The newly created child node.

#### Discussion

Use this method to specify a possible result of testing this node’s attribute (that is, an answer for this node’s question). The `attribute` parameter an have either of two kinds of values: if this test produces the decision tree’s final result (or action), the value identifies that action; if the next step in the decision tree is to be another question, the value identifies the next attribute to test (or question to ask).

This method adds a random branch to the decision tree; when you use the findActionForAnswers method, the tree tests the other attributes using the answers you specify in that method, but when it reaches an attribute with random branches, it chooses one randomly instead of testing the answer for that attribute. (To use random branching, you must set the [`randomSource`](gkdecisiontree/randomsource.md) property of the decision tree.) The `weight` parameter modifies the relative likelihood of each branch in a random set—branches with a higher weight are more likely than those with lower weights.

You can use this method to add some unpredictability to an otherwise deterministic decision; for example, a strategy combat game might use this method to choose an attack at random after other criteria have been satisfied. Here, the “Psychic Strike” attack will randomly occur 10% of the time (because its weight is 1 and the sum of all  weights for the node it branches from is 10):

## Parameters

- `weight`: The relative probability that a random choice should follow this branch.
- `attribute`: The attribute for the child node to create.

## See Also

- [func createBranch(value: NSNumber, attribute: any NSObjectProtocol) -> Self](gkdecisionnode/createbranch(value:attribute:).md)
  Creates a child node that the decision tree should use when the current node’s attribute has the specified value.
- [func createBranch(predicate: NSPredicate, attribute: any NSObjectProtocol) -> Self](gkdecisionnode/createbranch(predicate:attribute:).md)
  Creates a child node that the decision tree should use when the current node’s attribute satisfies the specified predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode/createbranch(weight:attribute:))*