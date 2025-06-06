# CFTreeGetChildAtIndex(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the child of a tree at the specified index.

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
func CFTreeGetChildAtIndex(_ tree: CFTree!, _ idx: CFIndex) -> CFTree!
```

#### Return Value

The child tree at `idx`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `tree`: The tree to examine.
- `idx`: The index of the child obtain. The value must be less than the number of children in  .

## See Also

- [func CFTreeFindRoot(CFTree!) -> CFTree!](cftreefindroot(_:).md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildCount(CFTree!) -> CFIndex](cftreegetchildcount(_:).md)
  Returns the number of children in a tree.
- [func CFTreeGetChildren(CFTree!, UnsafeMutablePointer<Unmanaged<CFTree>?>!)](cftreegetchildren(_:_:).md)
  Fills a buffer with children from the tree.
- [func CFTreeGetContext(CFTree!, UnsafeMutablePointer<CFTreeContext>!)](cftreegetcontext(_:_:).md)
  Returns the context of the specified tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](cftreegetfirstchild(_:).md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](cftreegetnextsibling(_:).md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](cftreegetparent(_:).md)
  Returns the parent of a given tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetchildatindex(_:_:))*