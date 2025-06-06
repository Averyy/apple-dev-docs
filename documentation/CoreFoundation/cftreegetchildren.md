# CFTreeGetChildren(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Fills a buffer with children from the tree.

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
func CFTreeGetChildren(_ tree: CFTree!, _ children: UnsafeMutablePointer<Unmanaged<CFTree>?>!)
```

## Parameters

- `tree`: The tree to examine.
- `children`: The C array of pointer-sized values to be filled with the children from  . This value must be a valid pointer to a C array of at least the size of the number of children in  . Use the   function to obtain the number of children in  . You are responsible for retaining and releasing the returned objects as needed.

## See Also

- [func CFTreeFindRoot(CFTree!) -> CFTree!](cftreefindroot(_:).md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](cftreegetchildatindex(_:_:).md)
  Returns the child of a tree at the specified index.
- [func CFTreeGetChildCount(CFTree!) -> CFIndex](cftreegetchildcount(_:).md)
  Returns the number of children in a tree.
- [func CFTreeGetContext(CFTree!, UnsafeMutablePointer<CFTreeContext>!)](cftreegetcontext(_:_:).md)
  Returns the context of the specified tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](cftreegetfirstchild(_:).md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](cftreegetnextsibling(_:).md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](cftreegetparent(_:).md)
  Returns the parent of a given tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreegetchildren(_:_:))*