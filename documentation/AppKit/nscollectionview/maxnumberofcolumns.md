# maxNumberOfColumns

**Framework**: AppKit  
**Kind**: property

The maximum number of columns that the collection view displays.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var maxNumberOfColumns: Int { get set }
```

#### Discussion

When the value of this property is `0`, the collection view has no maximum number of columns. The default value of this property is `0`.

It is possible for a collection view to specify both a maximum number of rows and a maximum number of columns. If the number of content objects exceeds the number of displayable items (*n*=`maxNumberOfRows` * `maxNumberOfColumns`) only the first *n* items of the content array are displayed.

## See Also

- [var itemPrototype: NSCollectionViewItem?](nscollectionview/itemprototype.md)
  The receiver’s collection view item prototype.
- [var maxNumberOfRows: Int](nscollectionview/maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var minItemSize: NSSize](nscollectionview/minitemsize.md)
  The minimum size (in points) of items in the collection view grid.
- [var maxItemSize: NSSize](nscollectionview/maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/maxnumberofcolumns)*