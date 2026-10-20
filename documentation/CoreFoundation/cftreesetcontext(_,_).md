# CFTreeSetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Replaces the context of a tree by releasing the old information pointer and retaining the new one.

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
func CFTreeSetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>!)
```

```c
extern void CFTreeSetContext(CFTreeRef tree, const CFTreeContext *context);
```

## Parameters

- `tree`: The tree to modify.
- `context`: The [`CFTreeContext`](./cftreecontext.md) structure to be copied and used as the context of the new tree. The information pointer will be retained by the tree if a retain function is provided. If this value is not a valid C pointer to a [`CFTreeContext`](./cftreecontext.md) structure-sized block of storage, the result is undefined. If the version number of the storage is not a valid [`CFTreeContext`](./cftreecontext.md) version number, the result is undefined.

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
- [func CFTreeRemove(CFTree!)](./cftreeremove%28_%29.md)
  Removes a tree from its parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreesetcontext(_:_:))*