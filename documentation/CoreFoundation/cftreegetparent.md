# CFTreeGetParent(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the parent of a given tree.

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
func CFTreeGetParent(_ tree: CFTree!) -> CFTree!
```

#### Return Value

The parent of `tree`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `tree`: The tree to examine.

## See Also

- [func CFTreeFindRoot(CFTree!) -> CFTree!](cftreefindroot(_:).md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](cftreegetchildatindex(_:_:).md)
  Returns the child of a tree at the specified index.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetparent(_:))*