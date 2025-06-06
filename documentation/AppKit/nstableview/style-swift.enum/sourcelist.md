# NSTableView.Style.sourceList

**Framework**: AppKit  
**Kind**: case

The table view style resolves to a source-list style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case sourceList
```

#### Discussion

A source-list style table adopts the standard metrics, row selection style, and background of a sidebar source list. In addition, an [`NSOutlineView`](nsoutlineview.md) with the source-list style adopts standard values for its [`indentationPerLevel`](nsoutlineview/indentationperlevel.md), [`rowHeight`](nstableview/rowheight.md), and [`intercellSpacing`](nstableview/intercellspacing.md) properties.

## See Also

- [NSTableView.Style.automatic](nstableview/style-swift.enum/automatic.md)
  The system resolves the table view style based on the table view hierarchy.
- [NSTableView.Style.fullWidth](nstableview/style-swift.enum/fullwidth.md)
  The table view style resolves to a full-width style.
- [NSTableView.Style.inset](nstableview/style-swift.enum/inset.md)
  The table view style resolves to an inset style.
- [NSTableView.Style.plain](nstableview/style-swift.enum/plain.md)
  The table view style resolves to a plain style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/style-swift.enum/sourcelist)*