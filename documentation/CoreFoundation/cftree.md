# CFTree

**Framework**: Core Foundation  
**Kind**: class

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
class CFTree
```

#### Overview

You use CFTree to create tree structures that represent hierarchical organizations of information. In such structures, each tree node has exactly one parent tree (except for the root tree, which has no parent) and can have multiple children. Each CFTree object in the structure has a context associated with it; this context includes some program-defined data as well as callbacks that operate on that data. The program-defined data is often used as the basis for determining where CFTree objects fit within the structure. All CFTree objects are mutable.

You create a CFTree object using the [`CFTreeCreate(_:_:)`](cftreecreate(_:_:).md) function. This function takes an allocator and pointer to a [`CFTreeGetContext(_:_:)`](cftreegetcontext(_:_:).md) structure as parameters. The [`CFTreeContext`](cftreecontext.md) structure contains the program-defined data and callbacks needed to describe, retain, and release that data. If you do not implement these callbacks, your program-defined data will not be retained or released when trees are added and removed from a parent.

Each CFTree object has a parent and list of children, all of which may be `NULL`. CFTree provides functions for adding and removing tree objects from the tree structure. Use the [`CFTreeAppendChild(_:_:)`](cftreeappendchild(_:_:).md), [`CFTreeInsertSibling(_:_:)`](cftreeinsertsibling(_:_:).md), or [`CFTreePrependChild(_:_:)`](cftreeprependchild(_:_:).md) functions to add trees to a tree structure, and the [`CFTreeRemove(_:)`](cftreeremove(_:).md) or [`CFTreeRemoveAllChildren(_:)`](cftreeremoveallchildren(_:).md) functions to remove trees.

For the purposes of memory management, CFTree can be thought of as a collection. Typically the only object that retains a child tree is its parent. Usually, therefore, when you remove a child tree from a tree, the child tree is destroyed. If you want to use a child tree after you remove it from its parent, you should retain the child tree first, prior to removing it.

Releasing a tree releases its child trees, and all of their child trees (recursively). Note also that the final release of a tree (when its retain count decreases to zero) causes all of its child trees, and all of their child trees (recursively), to be destroyed, regardless of their retain counts. Releasing a child that is still in a tree is therefore a programming error, and may cause your application to crash.

You can use any of the get functions (functions containing the word “Get”) to obtain the parent, children, or attributes of a tree. For example, use [`CFTreeGetChildAtIndex(_:_:)`](cftreegetchildatindex(_:_:).md) to obtain a child of a tree at a specified location. In common with other Core Foundation “Get” functions, these functions do not retain the tree that is returned. If you are making other modifications to the tree, you should either retain or make a deep copy of the child tree returned.

You can apply a function to all children of a tree using the [`CFTreeApplyFunctionToChildren(_:_:_:)`](cftreeapplyfunctiontochildren(_:_:_:).md) function, and sort children of a tree using the [`CFTreeSortChildren(_:_:_:)`](cftreesortchildren(_:_:_:).md) function.

## Topics

### Creating Trees
- [func CFTreeCreate(CFAllocator!, UnsafePointer<CFTreeContext>!) -> CFTree!](cftreecreate(_:_:).md)
  Creates a new CFTree object.
### Modifying a Tree
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
- [func CFTreeSetContext(CFTree!, UnsafePointer<CFTreeContext>!)](cftreesetcontext(_:_:).md)
  Replaces the context of a tree by releasing the old information pointer and retaining the new one.
### Sorting a Tree
- [func CFTreeSortChildren(CFTree!, CFComparatorFunction!, UnsafeMutableRawPointer!)](cftreesortchildren(_:_:_:).md)
  Sorts the immediate children of a tree using a specified comparator function.
### Examining a Tree
- [func CFTreeFindRoot(CFTree!) -> CFTree!](cftreefindroot(_:).md)
  Returns the root tree of a given tree.
- [func CFTreeGetChildAtIndex(CFTree!, CFIndex) -> CFTree!](cftreegetchildatindex(_:_:).md)
  Returns the child of a tree at the specified index.
- [func CFTreeGetChildCount(CFTree!) -> CFIndex](cftreegetchildcount(_:).md)
  Returns the number of children in a tree.
- [func CFTreeGetChildren(CFTree!, UnsafeMutablePointer<Unmanaged<CFTree>?>!)](cftreegetchildren(_:_:).md)
  Fills a buffer with children from the tree.
- [func CFTreeGetContext(CFTree!, UnsafeMutablePointer<CFTreeContext>!)](cftreegetcontext(_:_:).md)
  Returns the context of the specified tree.
- [func CFTreeGetFirstChild(CFTree!) -> CFTree!](cftreegetfirstchild(_:).md)
  Returns the first child of a tree.
- [func CFTreeGetNextSibling(CFTree!) -> CFTree!](cftreegetnextsibling(_:).md)
  Returns the next sibling, adjacent to a given tree, in the parent’s children list.
- [func CFTreeGetParent(CFTree!) -> CFTree!](cftreegetparent(_:).md)
  Returns the parent of a given tree.
### Performing an Operation on Tree Elements
- [func CFTreeApplyFunctionToChildren(CFTree!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cftreeapplyfunctiontochildren(_:_:_:).md)
  Calls a function once for each immediate child of a tree.
### Getting the Tree Type ID
- [func CFTreeGetTypeID() -> CFTypeID](cftreegettypeid().md)
  Returns the type identifier of the CFTree opaque type.
### Callbacks
- [typealias CFTreeApplierFunction](cftreeapplierfunction.md)
  Type of the callback function used by the CFTree apply function.
- [typealias CFTreeCopyDescriptionCallBack](cftreecopydescriptioncallback.md)
  Callback function used to provide a description of the program-defined information pointer.
- [typealias CFTreeReleaseCallBack](cftreereleasecallback.md)
  Callback function used to release a previously retained program-defined information pointer.
- [typealias CFTreeRetainCallBack](cftreeretaincallback.md)
  Callback function used to retain a program-defined information pointer.
### Data Types
- [struct CFTreeContext](cftreecontext.md)
  Structure containing program-defined data and callbacks for a CFTree object.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftree)*