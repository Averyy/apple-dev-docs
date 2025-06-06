# createBranch(value:attribute:)

**Framework**: GameplayKit  
**Kind**: method

Creates a child node that the decision tree should use when the current node’s attribute has the specified value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func createBranch(value: NSNumber, attribute: any NSObjectProtocol) -> Self
```

#### Return Value

The newly created child node.

#### Discussion

Use this method to specify a possible result of testing this node’s attribute (that is, an answer for this node’s question). The `attribute` parameter an have either of two kinds of values: if this test produces the decision tree’s final result (or action), the value identifies that action; if the next step in the decision tree is to be another question, the value identifies the next attribute to test (or question to ask).

The `value` parameter is a specific value for this node’s attribute, so this method is useful for questions that must have one of a few specific answers. (If a question has many possible answers, see the [`createBranch(predicate:attribute:)`](gkdecisionnode/createbranch(predicate:attribute:).md) method instead.) For example, a strategy combat game might use this method to choose an attack based on the type of opponent:

## Parameters

- `value`: The value for this node’s attribute that should result in following the newly created branch.
- `attribute`: The attribute for the child node to create.

## See Also

- [func createBranch(predicate: NSPredicate, attribute: any NSObjectProtocol) -> Self](gkdecisionnode/createbranch(predicate:attribute:).md)
  Creates a child node that the decision tree should use when the current node’s attribute satisfies the specified predicate.
- [func createBranch(weight: Int, attribute: any NSObjectProtocol) -> Self](gkdecisionnode/createbranch(weight:attribute:).md)
  Creates a child node that the decision tree should use as the result of a random choice, biased by the specified weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode/createbranch(value:attribute:))*