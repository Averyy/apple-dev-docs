# CFTreeSortChildren(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sorts the immediate children of a tree using a specified comparator function.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFTreeSortChildren(_ tree: CFTree!, _ comparator: CFComparatorFunction!, _ context: UnsafeMutableRawPointer!)
```

#### Discussion

Note that the comparator only operates one level deep and does not operate on descendants further removed than the immediate children of a tree node.

## Parameters

- `tree`: The tree to sort.
- `comparator`: The function with a comparator function type signature which is used in the sort operation to compare children of the tree. The children of the tree are sorted from least to greatest according to this function.
- `context`: A pointer-sized program-defined value that is passed to the comparator function, but is otherwise unused by this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreesortchildren(_:_:_:))*