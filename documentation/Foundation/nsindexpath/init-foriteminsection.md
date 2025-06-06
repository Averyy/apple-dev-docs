# init(forItem:inSection:)

**Framework**: Foundation  
**Kind**: init

Initializes an index path with the indexes of a specific item and section in a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(item: Int, section: Int)
```

#### Return Value

An [`NSIndexPath`](nsindexpath.md) object.

## Parameters

- `item`: An index number identifying an item in a   object in a section identified by the   parameter.
- `section`: An index number identifying a section in a   object.

## See Also

- [convenience init(forRow: Int, inSection: Int)](nsindexpath/init(forrow:insection:).md)
  Initializes an index path with the indexes of a specific row and section in a table view.
- [var section: Int](nsindexpath/section.md)
  An index number identifying a section in a table view or collection view.
- [var row: Int](nsindexpath/row.md)
  An index number identifying a row in a section of a table view.
- [var item: Int](nsindexpath/item.md)
  An index number identifying an item in a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/init(foritem:insection:))*