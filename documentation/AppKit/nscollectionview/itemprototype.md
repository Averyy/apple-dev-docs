# itemPrototype

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s collection view item prototype.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Use -registerNib:forItemWithIdentifier: or -registerClass:forItemWithIdentifier: instead.

## Declaration

```swift
var itemPrototype: NSCollectionViewItem? { get set }
```

```objc
@property (strong, nullable) NSCollectionViewItem * itemPrototype;
```

#### Discussion

Whenever possible, use a data source object to provide items. For more information, see the [`dataSource`](./datasource.md) property.

## See Also

### Deprecated properties
- [var maxNumberOfRows: Int](./maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var maxNumberOfColumns: Int](./maxnumberofcolumns.md)
  The maximum number of columns that the collection view displays.
- [var minItemSize: NSSize](./minitemsize.md)
  The minimum size (in points) of items in the collection view grid.
- [var maxItemSize: NSSize](./maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/itemprototype)*