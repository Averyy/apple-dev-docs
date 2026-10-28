# maxNumberOfColumns

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of columns that the collection view displays.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Use NSCollectionViewGridLayout as the receiver's collectionViewLayout, setting its maximumNumberOfColumns instead

## Declaration

```swift
var maxNumberOfColumns: Int { get set }
```

```objc
@property NSUInteger maxNumberOfColumns;
```

## Discussion

When the value of this property is `0`, the collection view has no maximum number of columns. The default value of this property is `0`.

It is possible for a collection view to specify both a maximum number of rows and a maximum number of columns. If the number of content objects exceeds the number of displayable items (*n*=`maxNumberOfRows` * `maxNumberOfColumns`) only the first *n* items of the content array are displayed.

## See Also

### Deprecated properties
- [var itemPrototype: NSCollectionViewItem?](./itemprototype.md)
  The receiver’s collection view item prototype.
- [var maxNumberOfRows: Int](./maxnumberofrows.md)
  The maximum number of rows that the collection view displays.
- [var minItemSize: NSSize](./minitemsize.md)
  The minimum size (in points) of items in the collection view grid.
- [var maxItemSize: NSSize](./maxitemsize.md)
  The maximum size (in points) of items in the collection view grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/maxnumberofcolumns)*