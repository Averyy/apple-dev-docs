# CFTreeSetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Replaces the context of a tree by releasing the old information pointer and retaining the new one.

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
func CFTreeSetContext(_ tree: CFTree!, _ context: UnsafePointer<CFTreeContext>!)
```

## Parameters

- `tree`: The tree to modify.
- `context`: The   structure to be copied and used as the context of the new tree. The information pointer will be retained by the tree if a retain function is provided. If this value is not a valid C pointer to a   structure-sized block of storage, the result is undefined. If the version number of the storage is not a valid   version number, the result is undefined.

## See Also

- [func CFTreeAppendChild(CFTree!, CFTree!)](cftreeappendchild(_:_:).md)
  Adds a new child to a tree as the last in its list of children.
- [func CFTreeInsertSibling(CFTree!, CFTree!)](cftreeinsertsibling(_:_:).md)
  Inserts a new sibling after a given tree.
- [func CFTreeRemoveAllChildren(CFTree!)](cftreeremoveallchildren(_:).md)
  Removes all the children of a tree.
- [func CFTreePrependChild(CFTree!, CFTree!)](cftreeprependchild(_:_:).md)
  Adds a new child to the specified tree as the first in its list of children.
- [func CFTreeRemove(CFTree!)](cftreeremove(_:).md)
  Removes a tree from its parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreesetcontext(_:_:))*