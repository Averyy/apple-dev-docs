# NSIndexPath

**Framework**: Foundation  
**Kind**: class

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

#### Overview

In Swift, this object bridges to [`IndexPath`](indexpath.md); use [`NSIndexPath`](nsindexpath.md) when you need reference semantics or other Foundation-specific behavior.

Each index in an index path represents the index into an array of children from one node in the tree to another, deeper, node. For example, the index path `1.4.3.2` specifies the path shown in [`Figure 1`](nsindexpath#1965825.md).

![Index path “1.4.3.2”](https://docs-assets.developer.apple.com/published/3a94cb2adc36a5b685ea3a727e5ba729/media-1965825.gif)

> **Note**:  The UIKit framework adds programming interfaces to the `NSIndexPath` class of the Foundation framework to facilitate the identification of rows and sections in [`UITableView`](https://developer.apple.com/documentation/UIKit/UITableView) objects and the identification of items and sections in [`UICollectionView`](https://developer.apple.com/documentation/UIKit/UICollectionView) objects. The API consists of class factory methods and properties for accessing the various indexed values. You use the factory methods to create an index path for the corresponding table view or collection view.

 The UIKit framework adds programming interfaces to the `NSIndexPath` class of the Foundation framework to facilitate the identification of rows and sections in [`UITableView`](https://developer.apple.com/documentation/UIKit/UITableView) objects and the identification of items and sections in [`UICollectionView`](https://developer.apple.com/documentation/UIKit/UICollectionView) objects. The API consists of class factory methods and properties for accessing the various indexed values. You use the factory methods to create an index path for the corresponding table view or collection view.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`IndexPath`](indexpath.md) structure, which bridges to the [`NSIndexPath`](nsindexpath.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`IndexPath`](indexpath.md) structure, which bridges to the [`NSIndexPath`](nsindexpath.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating and Initializing Index Paths
- [convenience init(index: Int)](nsindexpath/init(index:).md)
  Initializes an index path with a single node.
- [init(indexes: UnsafePointer<Int>?, length: Int)](nsindexpath/init(indexes:length:).md)
  Initializes an index path with the given nodes and length.
### Using Special Node Names
- [convenience init(forRow: Int, inSection: Int)](nsindexpath/init(forrow:insection:).md)
  Initializes an index path with the indexes of a specific row and section in a table view.
- [convenience init(forItem: Int, inSection: Int)](nsindexpath/init(foritem:insection:).md)
  Initializes an index path with the indexes of a specific item and section in a collection view.
- [var section: Int](nsindexpath/section.md)
  An index number identifying a section in a table view or collection view.
- [var row: Int](nsindexpath/row.md)
  An index number identifying a row in a section of a table view.
- [var item: Int](nsindexpath/item.md)
  An index number identifying an item in a section of a collection view.
### Counting Nodes
- [var length: Int](nsindexpath/length.md)
  The number of nodes in the index path.
### Adding and Removing Nodes
- [func adding(Int) -> IndexPath](nsindexpath/adding(_:).md)
  Returns an index path containing the nodes in the receiving index path plus another given index.
- [func removingLastIndex() -> IndexPath](nsindexpath/removinglastindex.md)
  Returns an index path with the nodes in the receiving index path, excluding the last one.
### Comparing Index Paths
- [func compare(IndexPath) -> ComparisonResult](nsindexpath/compare(_:).md)
  Indicates the depth-first traversal order of the receiving index path and another index path.
### Working with Indexes
- [func index(atPosition: Int) -> Int](nsindexpath/index(atposition:).md)
  Provides the value at a particular node in the index path.
- [func getIndexes(UnsafeMutablePointer<Int>, range: NSRange)](nsindexpath/getindexes(_:range:).md)
  Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.
- [func getIndexes(UnsafeMutablePointer<Int>)](nsindexpath/getindexes(_:).md)
  Copies the objects contained in the index path into indexes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath)*