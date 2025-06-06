# CFTreeRemove(_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a tree from its parent.

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
func CFTreeRemove(_ tree: CFTree!)
```

#### Discussion

When a child tree is removed from its parent, the parent releases it. If you want to use the child after you have removed it, you should ensure you retain it before removing it from its parent.

## Parameters

- `tree`: The tree to remove from its parent.

## See Also

- [func CFTreeAppendChild(CFTree!, CFTree!)](cftreeappendchild(_:_:).md)
  Adds a new child to a tree as the last in its list of children.
- [func CFTreeInsertSibling(CFTree!, CFTree!)](cftreeinsertsibling(_:_:).md)
  Inserts a new sibling after a given tree.
- [func CFTreeRemoveAllChildren(CFTree!)](cftreeremoveallchildren(_:).md)
  Removes all the children of a tree.
- [func CFTreePrependChild(CFTree!, CFTree!)](cftreeprependchild(_:_:).md)
  Adds a new child to the specified tree as the first in its list of children.
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](cftreesetcontext(_:_:).md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeremove(_:))*