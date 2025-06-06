# maximumNumberOfColumns

**Framework**: AppKit  
**Kind**: property

The maximum number of columns to display in the collection view’s visible area.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var maximumNumberOfColumns: Int { get set }
```

#### Discussion

Use this value to specify the maximum number of columns that should be visible in the collection view at any given time. The grid layout object uses this value during layout to configure the position and spacing of items. The default value of this property is `0`, which means that there is no maximum number of columns.

## See Also

- [var maximumNumberOfRows: Int](nscollectionviewgridlayout/maximumnumberofrows.md)
  The maximum number of rows to display in the collection view’s visible area.
- [var minimumItemSize: NSSize](nscollectionviewgridlayout/minimumitemsize.md)
  The smallest allowable size for an item’s view.
- [var maximumItemSize: NSSize](nscollectionviewgridlayout/maximumitemsize.md)
  The largest allowable size for an item’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewgridlayout/maximumnumberofcolumns)*