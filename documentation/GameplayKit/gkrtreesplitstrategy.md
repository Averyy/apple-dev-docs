# GKRTreeSplitStrategy

**Framework**: GameplayKit  
**Kind**: enum

Options that control how a tree balances its internal structure when adding elements, used with the [`addElement(_:boundingRectMin:boundingRectMax:splitStrategy:)`](gkrtree/addelement(_:boundingrectmin:boundingrectmax:splitstrategy:).md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum GKRTreeSplitStrategy
```

## Topics

### Constants
- [GKRTreeSplitStrategy.halve](gkrtreesplitstrategy/halve.md)
  An option to split groups of elements in half based on the order they were added to the tree in.
- [GKRTreeSplitStrategy.linear](gkrtreesplitstrategy/linear.md)
  An option to split groups of elements by finding a line that divides space so that half of the elements are on either side.
- [GKRTreeSplitStrategy.quadratic](gkrtreesplitstrategy/quadratic.md)
  An option to split groups of elements by finding the subgroups that occupy the least area.
- [GKRTreeSplitStrategy.reduceOverlap](gkrtreesplitstrategy/reduceoverlap.md)
  An option to split groups of elements by finding the subgroups whose areas overlap the least.
### Initializers
- [init?(rawValue: Int)](gkrtreesplitstrategy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrtreesplitstrategy)*