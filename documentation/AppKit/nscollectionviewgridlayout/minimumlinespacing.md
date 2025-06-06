# minimumLineSpacing

**Framework**: AppKit  
**Kind**: property

The minimum spacing (in points) to use between rows or columns.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var minimumLineSpacing: CGFloat { get set }
```

#### Discussion

For a vertically scrolling layout, the value represents the minimum spacing between successive rows. For a horizontally scrolling layout, the value represents the minimum spacing between successive columns. This spacing is not applied to the space between the header view and the first line or between the last line and the footer view.

The default value of this property is `0.0`.

## See Also

- [var minimumInteritemSpacing: CGFloat](nscollectionviewgridlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var margins: NSEdgeInsets](nscollectionviewgridlayout/margins.md)
  The amount of empty space (in points) around the grid’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewgridlayout/minimumlinespacing)*