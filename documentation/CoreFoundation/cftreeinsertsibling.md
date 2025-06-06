# CFTreeInsertSibling(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Inserts a new sibling after a given tree.

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
func CFTreeInsertSibling(_ tree: CFTree!, _ newSibling: CFTree!)
```

#### Discussion

When a child tree is added to another tree, the child tree is retained by its new parent.

If you want to manipulate an existing tree structure, since `newSibling` must not have a parent you need to remove a tree from its parent in order to move it to a new position. If you do this, you should retain the tree before you actually remove it from its parent (see [`CFTreeRemove(_:)`](cftreeremove(_:).md)).

## Parameters

- `tree`: The tree after which to insert  .   must have a parent.
- `newSibling`: The sibling to add.   must not have a parent.

## See Also

- [func CFTreeAppendChild(CFTree!, CFTree!)](cftreeappendchild(_:_:).md)
  Adds a new child to a tree as the last in its list of children.
- [func CFTreeRemoveAllChildren(CFTree!)](cftreeremoveallchildren(_:).md)
  Removes all the children of a tree.
- [func CFTreePrependChild(CFTree!, CFTree!)](cftreeprependchild(_:_:).md)
  Adds a new child to the specified tree as the first in its list of children.
- [func CFTreeRemove(CFTree!)](cftreeremove(_:).md)
  Removes a tree from its parent.
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](cftreesetcontext(_:_:).md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeinsertsibling(_:_:))*