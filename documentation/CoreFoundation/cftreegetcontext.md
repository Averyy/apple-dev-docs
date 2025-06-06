# CFTreeGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the context of the specified tree.

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
func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafeMutablePointer<CFTreeContext>!)
```

## Parameters

- `tree`: The tree to examine.
- `context`: The   structure to be filled in with the context of the specified tree. This value must be a valid C pointer to a   structure-sized block of storage. If the version number of the storage is not a valid   structure version number, the result is undefined.

## See Also

- [func CFTreeFindRoot(CFTree!) -> CFTree!](cftreefindroot(_:).md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](cftreegetchildatindex(_:_:).md)
  Returns the child of a tree at the specified index.
- [func CFTreeGetChildCount(CFTree!) -> CFIndex](cftreegetchildcount(_:).md)
  Returns the number of children in a tree.
- [func CFTreeGetChildren(CFTree!, UnsafeMutablePointer<Unmanaged<CFTree>?>!)](cftreegetchildren(_:_:).md)
  Fills a buffer with children from the tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](cftreegetfirstchild(_:).md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](cftreegetnextsibling(_:).md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](cftreegetparent(_:).md)
  Returns the parent of a given tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetcontext(_:_:))*