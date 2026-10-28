# NSIndexPath

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A list of indexes that together represent the path to a specific location in a tree of nested arrays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSIndexPath
```

```objc
@interface NSIndexPath : NSObject
```

## Overview

In Swift, this object bridges to [`IndexPath`](./indexpath.md); use [`NSIndexPath`](./nsindexpath.md) when you need reference semantics or other Foundation-specific behavior.

Each index in an index path represents the index into an array of children from one node in the tree to another, deeper, node. For example, the index path `1.4.3.2` specifies the path shown in [Figure 1](./nsindexpath.md#1965825).

![Index path “1.4.3.2”](https://developer.apple.com/tutorials/images/com.apple.foundation/media-1965825.gif)

> **Note**:  The UIKit framework adds programming interfaces to the `NSIndexPath` class of the Foundation framework to facilitate the identification of rows and sections in [`UITableView`](../UIKit/uitableview.md) objects and the identification of items and sections in [`UICollectionView`](../UIKit/uicollectionview.md) objects. The API consists of class factory methods and properties for accessing the various indexed values. You use the factory methods to create an index path for the corresponding table view or collection view.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexPath`](./indexpath.md) structure, which bridges to the [`NSIndexPath`](./nsindexpath.md) class. For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Creating and Initializing Index Paths
- [convenience init(index: Int)](./nsindexpath/init%28index%29.md)
  Initializes an index path with a single node.
- [init(indexes: UnsafePointer<Int>?, length: Int)](./nsindexpath/init%28indexes,length%29.md)
  Initializes an index path with the given nodes and length.
- [+ indexPathWithIndex:](./nsindexpath/indexpathwithindex_.md)
  Creates a one-node index path.
- [+ indexPathWithIndexes:length:](./nsindexpath/indexpathwithindexes_length_.md)
  Creates an index path with one or more nodes.
### Using Special Node Names
- [convenience init(forRow: Int, inSection: Int)](./nsindexpath/init%28forrow,insection%29.md)
  Initializes an index path with the indexes of a specific row and section in a table view.
- [convenience init(forItem: Int, inSection: Int)](./nsindexpath/init%28foritem,insection%29.md)
  Initializes an index path with the indexes of a specific item and section in a collection view.
- [var section: Int](./nsindexpath/section.md)
  An index number identifying a section in a table view or collection view.
- [var row: Int](./nsindexpath/row.md)
  An index number identifying a row in a section of a table view.
- [var item: Int](./nsindexpath/item.md)
  An index number identifying an item in a section of a collection view.
### Counting Nodes
- [var length: Int](./nsindexpath/length.md)
  The number of nodes in the index path.
### Adding and Removing Nodes
- [func adding(Int) -> IndexPath](./nsindexpath/adding%28_%29.md)
  Returns an index path containing the nodes in the receiving index path plus another given index.
- [func removingLastIndex() -> IndexPath](./nsindexpath/removinglastindex%28%29.md)
  Returns an index path with the nodes in the receiving index path, excluding the last one.
### Comparing Index Paths
- [func compare(IndexPath) -> ComparisonResult](./nsindexpath/compare%28_%29.md)
  Indicates the depth-first traversal order of the receiving index path and another index path.
### Working with Indexes
- [func index(atPosition: Int) -> Int](./nsindexpath/index%28atposition%29.md)
  Provides the value at a particular node in the index path.
- [func getIndexes(UnsafeMutablePointer<Int>, range: NSRange)](./nsindexpath/getindexes%28_,range%29.md)
  Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.
- [func getIndexes(UnsafeMutablePointer<Int>)](./nsindexpath/getindexes%28_%29.md)
  Copies the objects contained in the index path into indexes.
### Initializers
- [init?(coder: NSCoder)](./nsindexpath/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Indexes
- [NSIndexSet](./nsindexset.md)
  An immutable collection of unique integer values that represent indexes in another collection.
- [NSMutableIndexSet](./nsmutableindexset.md)
  A mutable collection of unique integer values that represent indexes in another collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath)*