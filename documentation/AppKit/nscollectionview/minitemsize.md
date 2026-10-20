# minItemSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum size (in points) of items in the collection view grid.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Use NSCollectionViewGridLayout as the receiver's collectionViewLayout, setting its minimumItemSize instead

## Declaration

```swift
var minItemSize: NSSize { get set }
```

```objc
@property NSSize minItemSize;
```

#### Discussion

The default value of this property is (`0`, `0`). If the item’s view is resizable, set the value to the minimum size that the view should use.

## See Also

### Deprecated properties
- [var itemPrototype: NSCollectionViewItem?](./itemprototype.md)
  The receiver’s collection view item prototype.
- [var maxNumberOfRows: Int](./maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var maxNumberOfColumns: Int](./maxnumberofcolumns.md)
  The maximum number of columns that the collection view displays.
- [var maxItemSize: NSSize](./maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/minitemsize)*