# init(forRow:inSection:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an index path with the indexes of a specific row and section in a table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(forRow row: Int, inSection section: Int)
```

```swift
convenience init(row: Int, section: Int)
```

```objc
+ (instancetype) indexPathForRow:(NSInteger) row inSection:(NSInteger) section;
```

## Return Value

An [`NSIndexPath`](../nsindexpath.md) object.

## Parameters

- `row`: An index number identifying a row in a [`UITableView`](../../UIKit/uitableview.md) object in a section identified by `section`.
- `section`: An index number identifying a section in a [`UITableView`](../../UIKit/uitableview.md) object.

## See Also

### Using Special Node Names
- [convenience init(forItem: Int, inSection: Int)](./init%28foritem,insection%29.md)
  Initializes an index path with the indexes of a specific item and section in a collection view.
- [var section: Int](./section.md)
  An index number identifying a section in a table view or collection view.
- [var row: Int](./row.md)
  An index number identifying a row in a section of a table view.
- [var item: Int](./item.md)
  An index number identifying an item in a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/init(forrow:insection:))*