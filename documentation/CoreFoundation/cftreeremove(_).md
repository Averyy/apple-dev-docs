# CFTreeRemove(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a tree from its parent.

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
func CFTreeRemove(_ tree: CFTree!)
```

```c
extern void CFTreeRemove(CFTreeRef tree);
```

## Discussion

When a child tree is removed from its parent, the parent releases it. If you want to use the child after you have removed it, you should ensure you retain it before removing it from its parent.

## Parameters

- `tree`: The tree to remove from its parent.

## See Also

### Modifying a Tree
- [func CFTreeAppendChild(CFTree!, CFTree!)](./cftreeappendchild%28_,_%29.md)
  Adds a new child to a tree as the last in its list of children.
- [func CFTreeInsertSibling(CFTree!, CFTree!)](./cftreeinsertsibling%28_,_%29.md)
  Inserts a new sibling after a given tree.
- [func CFTreeRemoveAllChildren(CFTree!)](./cftreeremoveallchildren%28_%29.md)
  Removes all the children of a tree.
- [func CFTreePrependChild(CFTree!, CFTree!)](./cftreeprependchild%28_,_%29.md)
  Adds a new child to the specified tree as the first in its list of children.
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](./cftreesetcontext%28_,_%29.md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeremove(_:))*