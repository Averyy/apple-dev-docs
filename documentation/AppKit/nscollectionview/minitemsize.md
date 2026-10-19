# minItemSize

**Framework**: AppKit  
**Kind**: property

The minimum size (in points) of items in the collection view grid.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var minItemSize: NSSize { get set }
```

#### Discussion

The default value of this property is (`0`, `0`). If the item’s view is resizable, set the value to the minimum size that the view should use.

## See Also

- [var itemPrototype: NSCollectionViewItem?](nscollectionview/itemprototype.md)
  The receiver’s collection view item prototype.
- [var maxNumberOfRows: Int](nscollectionview/maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var maxNumberOfColumns: Int](nscollectionview/maxnumberofcolumns.md)
  The maximum number of columns that the collection view displays.
- [var maxItemSize: NSSize](nscollectionview/maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/minitemsize)*