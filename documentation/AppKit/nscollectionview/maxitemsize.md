# maxItemSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum size (in points) of items in the collection view grid.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Use NSCollectionViewGridLayout as the receiver's collectionViewLayout, setting its maximumItemSize instead

## Declaration

```swift
var maxItemSize: NSSize { get set }
```

```objc
@property NSSize maxItemSize;
```

#### Discussion

Setting the size to (`0`, `0`) means that there is no maximum grid size. The default value of this property is (`0`, `0`). If an item’s view  is resizable, set the value to the maximum size that the view should use.

## See Also

### Deprecated properties
- [var itemPrototype: NSCollectionViewItem?](./itemprototype.md)
  The receiver’s collection view item prototype.
- [var maxNumberOfRows: Int](./maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var maxNumberOfColumns: Int](./maxnumberofcolumns.md)
  The maximum number of columns that the collection view displays.
- [var minItemSize: NSSize](./minitemsize.md)
  The minimum size (in points) of items in the collection view grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/maxitemsize)*