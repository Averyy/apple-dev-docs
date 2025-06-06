# init(forRow:inSection:)

**Framework**: Foundation  
**Kind**: init

Initializes an index path with the indexes of a specific row and section in a table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(row: Int, section: Int)
```

#### Return Value

An [`NSIndexPath`](nsindexpath.md) object.

## Parameters

- `row`: An index number identifying a row in a   object in a section identified by  .
- `section`: An index number identifying a section in a   object.

## See Also

- [convenience init(forItem: Int, inSection: Int)](nsindexpath/init(foritem:insection:).md)
  Initializes an index path with the indexes of a specific item and section in a collection view.
- [var section: Int](nsindexpath/section.md)
  An index number identifying a section in a table view or collection view.
- [var row: Int](nsindexpath/row.md)
  An index number identifying a row in a section of a table view.
- [var item: Int](nsindexpath/item.md)
  An index number identifying an item in a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/init(forrow:insection:))*