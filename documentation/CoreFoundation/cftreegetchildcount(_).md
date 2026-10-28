# CFTreeGetChildCount(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of children in a tree.

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
func CFTreeGetChildCount(_ tree: CFTree!) -> CFIndex
```

```c
extern CFIndex CFTreeGetChildCount(CFTreeRef tree);
```

## Return Value

The number of children in `tree`.

## Parameters

- `tree`: The tree to examine.

## See Also

### Examining a Tree
- [func CFTreeFindRoot(CFTree!) -> CFTree!](./cftreefindroot%28_%29.md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](./cftreegetchildatindex%28_,_%29.md)
  Returns the child of a tree at the specified index.
- [func CFTreeGetChildren(CFTree!, UnsafeMutablePointer<Unmanaged<CFTree>?>!)](./cftreegetchildren%28_,_%29.md)
  Fills a buffer with children from the tree.
- [func CFTreeGetContext(CFTree!, UnsafeMutablePointer<CFTreeContext>!)](./cftreegetcontext%28_,_%29.md)
  Returns the context of the specified tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](./cftreegetfirstchild%28_%29.md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](./cftreegetnextsibling%28_%29.md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](./cftreegetparent%28_%29.md)
  Returns the parent of a given tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetchildcount(_:))*