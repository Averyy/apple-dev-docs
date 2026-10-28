# init(maxNumberOfChildren:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a new R-tree object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(maxNumberOfChildren: Int)
```

```objc
- (instancetype) initWithMaxNumberOfChildren:(NSUInteger) maxNumberOfChildren;
```

## Return Value

A new R-tree object.

## Discussion

An R-tree, like other tree data structures, is a collection of nodes, each of which contains one of the objects stored in the tree. You don’t directly interact with nodes—GameplayKit automatically creates and manages them, so you interact only with the objects the nodes contain. However, the `maxNumberOfChildren` parameter determines when the R-tree automatically reorganizes its internal structure, and thus the performance of the add and search operations.

A larger `maxNumberOfChildren` value means that the tree reorganizes itself less often. Therefore, the performance of the [`addElement(_:boundingRectMin:boundingRectMax:splitStrategy:)`](./addelement%28_,boundingrectmin,boundingrectmax,splitstrategy%29.md) method is faster (on average, across many calls). But because each node contains a larger number of elements, the performance of the [`elements(inBoundingRectMin:rectMax:)`](./elements%28inboundingrectmin,rectmax%29.md) method is slower (on average). A smaller `maxNumberOfChildren` value reverses the situation, improving performance for search operations at the cost of performance for add operations.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `maxNumberOfChildren`: The maximum number of children for each tree node.

## See Also

### Creating an R-Tree
- [+ treeWithMaxNumberOfChildren:](./treewithmaxnumberofchildren_.md)
  Creates a new R-tree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrtree/init(maxnumberofchildren:))*