# CFTreePrependChild(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a new child to the specified tree as the first in its list of children.

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
func CFTreePrependChild(_ tree: CFTree!, _ newChild: CFTree!)
```

#### Discussion

When a child tree is added to another tree, the child tree is retained by its new parent.

## Parameters

- `tree`: The tree to which to add  .
- `newChild`: The child tree to add to  . This value must not be a child of another tree.

## See Also

- [func CFTreeAppendChild(CFTree!, CFTree!)](cftreeappendchild(_:_:).md)
  Adds a new child to a tree as the last in its list of children.
- [func CFTreeInsertSibling(CFTree!, CFTree!)](cftreeinsertsibling(_:_:).md)
  Inserts a new sibling after a given tree.
- [func CFTreeRemoveAllChildren(CFTree!)](cftreeremoveallchildren(_:).md)
  Removes all the children of a tree.
- [func CFTreeRemove(CFTree!)](cftreeremove(_:).md)
  Removes a tree from its parent.
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](cftreesetcontext(_:_:).md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeprependchild(_:_:))*