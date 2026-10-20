# row

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSInteger row;
```

#### Discussion

The section the row is in is identified by the value of [`section`](./section.md).

## See Also

### Using Special Node Names
- [convenience init(forRow: Int, inSection: Int)](./init%28forrow,insection%29.md)
  Initializes an index path with the indexes of a specific row and section in a table view.
- [convenience init(forItem: Int, inSection: Int)](./init%28foritem,insection%29.md)
  Initializes an index path with the indexes of a specific item and section in a collection view.
- [var section: Int](./section.md)
  An index number identifying a section in a table view or collection view.
- [var item: Int](./item.md)
  An index number identifying an item in a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/row)*