# maximumItemSize

**Framework**: AppKit  
**Kind**: property

The largest allowable size for an item’s view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var maximumItemSize: NSSize { get set }
```

#### Discussion

Use this property to limit the maximum size of items displayed in the grid. The default value of this property is (`0.0`, `0.0`), which imposes no maximum size for items.

## See Also

- [var maximumNumberOfRows: Int](nscollectionviewgridlayout/maximumnumberofrows.md)
  The maximum number of rows to display in the collection view’s visible area.
- [var maximumNumberOfColumns: Int](nscollectionviewgridlayout/maximumnumberofcolumns.md)
  The maximum number of columns to display in the collection view’s visible area.
- [var minimumItemSize: NSSize](nscollectionviewgridlayout/minimumitemsize.md)
  The smallest allowable size for an item’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewgridlayout/maximumitemsize)*