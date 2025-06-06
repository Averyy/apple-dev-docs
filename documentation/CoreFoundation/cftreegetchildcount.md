# CFTreeGetChildCount(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of children in a tree.

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
func CFTreeGetChildCount(_ tree: CFTree!) -> CFIndex
```

#### Return Value

The number of children in `tree`.

## Parameters

- `tree`: The tree to examine.

## See Also

- [func CFTreeFindRoot(CFTree!) -> CFTree!](cftreefindroot(_:).md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](cftreegetchildatindex(_:_:).md)
  Returns the child of a tree at the specified index.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetchildcount(_:))*