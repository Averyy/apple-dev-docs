# init(forItem:inSection:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an index path with the indexes of a specific item and section in a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
convenience init(forItem item: Int, inSection section: Int)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
convenience init(item: Int, section: Int)
```

*macOS*

```swift
init(forItem item: Int, inSection section: Int)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (instancetype) indexPathForItem:(NSInteger) item inSection:(NSInteger) section;
```

*macOS*

```objc
+ (NSIndexPath *) indexPathForItem:(NSInteger) item inSection:(NSInteger) section;
```

#### Return Value

An [`NSIndexPath`](../nsindexpath.md) object.

## Parameters

- `item`: An index number identifying an item in a [`UICollectionView`](../../UIKit/uicollectionview.md) object in a section identified by the `section` parameter.
- `section`: An index number identifying a section in a [`UICollectionView`](../../UIKit/uicollectionview.md) object.

## See Also

### Using Special Node Names
- [convenience init(forRow: Int, inSection: Int)](./init%28forrow,insection%29.md)
  Initializes an index path with the indexes of a specific row and section in a table view.
- [var section: Int](./section.md)
  An index number identifying a section in a table view or collection view.
- [var row: Int](./row.md)
  An index number identifying a row in a section of a table view.
- [var item: Int](./item.md)
  An index number identifying an item in a section of a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/init(foritem:insection:))*