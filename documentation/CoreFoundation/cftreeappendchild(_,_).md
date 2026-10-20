# CFTreeAppendChild(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a new child to a tree as the last in its list of children.

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
func CFTreeAppendChild(_ tree: CFTree!, _ newChild: CFTree!)
```

```c
extern void CFTreeAppendChild(CFTreeRef tree, CFTreeRef newChild);
```

#### Discussion

When a child tree is added to another tree, the child tree is retained by its new parent.

## Parameters

- `tree`: The tree to which to add `newChild`.
- `newChild`: The child tree to add to `tree`. If this parameter is a tree which is already a child of any other tree, the behavior is undefined.

## See Also

### Modifying a Tree
- [func CFTreeInsertSibling(CFTree!, CFTree!)](./cftreeinsertsibling%28_,_%29.md)
  Inserts a new sibling after a given tree.
- [func CFTreeRemoveAllChildren(CFTree!)](./cftreeremoveallchildren%28_%29.md)
  Removes all the children of a tree.
- [func CFTreePrependChild(CFTree!, CFTree!)](./cftreeprependchild%28_,_%29.md)
  Adds a new child to the specified tree as the first in its list of children.
- [func CFTreeRemove(CFTree!)](./cftreeremove%28_%29.md)
  Removes a tree from its parent.
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](./cftreesetcontext%28_,_%29.md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeappendchild(_:_:))*