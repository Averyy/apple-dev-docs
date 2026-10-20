# CFTreeRemoveAllChildren(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes all the children of a tree.

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
func CFTreeRemoveAllChildren(_ tree: CFTree!)
```

```c
extern void CFTreeRemoveAllChildren(CFTreeRef tree);
```

## Parameters

- `tree`: The tree to modify.

## See Also

### Modifying a Tree
- [func CFTreeAppendChild(CFTree!, CFTree!)](./cftreeappendchild%28_,_%29.md)
  Adds a new child to a tree as the last in its list of children.
- [func CFTreeInsertSibling(CFTree!, CFTree!)](./cftreeinsertsibling%28_,_%29.md)
  Inserts a new sibling after a given tree.
- [func CFTreePrependChild(CFTree!, CFTree!)](./cftreeprependchild%28_,_%29.md)
  Adds a new child to the specified tree as the first in its list of children.
- [func CFTreeRemove(CFTree!)](./cftreeremove%28_%29.md)
  Removes a tree from its parent.
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](./cftreesetcontext%28_,_%29.md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeremoveallchildren(_:))*