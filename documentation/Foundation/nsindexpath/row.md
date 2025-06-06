# row

**Framework**: Foundation  
**Kind**: property

An index number identifying a row in a section of a table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var row: Int { get }
```

#### Discussion

The section the row is in is identified by the value of [`section`](nsindexpath/section.md).

## See Also

- [convenience init(forRow: Int, inSection: Int)](nsindexpath/init(forrow:insection:).md)
  Initializes an index path with the indexes of a specific row and section in a table view.
- [convenience init(forItem: Int, inSection: Int)](nsindexpath/init(foritem:insection:).md)
  Initializes an index path with the indexes of a specific item and section in a collection view.
- [var section: Int](nsindexpath/section.md)
  An index number identifying a section in a table view or collection view.
- [var item: Int](nsindexpath/item.md)
  An index number identifying an item in a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/row)*