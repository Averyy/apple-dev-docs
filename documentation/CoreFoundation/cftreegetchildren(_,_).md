# CFTreeGetChildren(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Fills a buffer with children from the tree.

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
func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafeMutablePointer<Unmanaged<CFTree>?>!)
```

```c
extern void CFTreeGetChildren(CFTreeRef tree, CFTreeRef*children);
```

## Parameters

- `tree`: The tree to examine.
- `children`: The C array of pointer-sized values to be filled with the children from `tree`. This value must be a valid pointer to a C array of at least the size of the number of children in `tree`. Use the [`CFTreeGetChildCount(_:)`](./cftreegetchildcount%28_%29.md) function to obtain the number of children in `tree`. You are responsible for retaining and releasing the returned objects as needed.

## See Also

### Examining a Tree
- [func CFTreeFindRoot(CFTree!) -> CFTree!](./cftreefindroot%28_%29.md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](./cftreegetchildatindex%28_,_%29.md)
  Returns the child of a tree at the specified index.
- [func CFTreeGetChildCount(CFTree!) -> CFIndex](./cftreegetchildcount%28_%29.md)
  Returns the number of children in a tree.
- [func CFTreeGetContext(CFTree!, UnsafeMutablePointer<CFTreeContext>!)](./cftreegetcontext%28_,_%29.md)
  Returns the context of the specified tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](./cftreegetfirstchild%28_%29.md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](./cftreegetnextsibling%28_%29.md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](./cftreegetparent%28_%29.md)
  Returns the parent of a given tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetchildren(_:_:))*