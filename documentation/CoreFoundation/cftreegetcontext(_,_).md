# CFTreeGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the context of the specified tree.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFTreeGetContext(_ tree: CFTree!, _ context: UnsafeMutablePointer<CFTreeContext>!)
```

```c
extern void CFTreeGetContext(CFTreeRef tree, CFTreeContext *context);
```

## Parameters

- `tree`: The tree to examine.
- `context`: The [`CFTreeContext`](./cftreecontext.md) structure to be filled in with the context of the specified tree. This value must be a valid C pointer to a [`CFTreeContext`](./cftreecontext.md) structure-sized block of storage. If the version number of the storage is not a valid [`CFTreeContext`](./cftreecontext.md) structure version number, the result is undefined.

## See Also

### Examining a Tree
- [func CFTreeFindRoot(CFTree!) -> CFTree!](./cftreefindroot%28_%29.md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](./cftreegetchildatindex%28_,_%29.md)
  Returns the child of a tree at the specified index.
- [func CFTreeGetChildCount(CFTree!) -> CFIndex](./cftreegetchildcount%28_%29.md)
  Returns the number of children in a tree.
- [func CFTreeGetChildren(CFTree!, UnsafeMutablePointer<Unmanaged<CFTree>?>!)](./cftreegetchildren%28_,_%29.md)
  Fills a buffer with children from the tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](./cftreegetfirstchild%28_%29.md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](./cftreegetnextsibling%28_%29.md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](./cftreegetparent%28_%29.md)
  Returns the parent of a given tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetcontext(_:_:))*