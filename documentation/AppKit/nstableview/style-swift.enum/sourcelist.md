# NSTableView.Style.sourceList

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The table view style resolves to a source-list style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case sourceList
```

```c
NSTableViewStyleSourceList
```

## Discussion

A source-list style table adopts the standard metrics, row selection style, and background of a sidebar source list. In addition, an [`NSOutlineView`](../../nsoutlineview.md) with the source-list style adopts standard values for its [`indentationPerLevel`](../../nsoutlineview/indentationperlevel.md), [`rowHeight`](../rowheight.md), and [`intercellSpacing`](../intercellspacing.md) properties.

## See Also

### Table Styles
- [NSTableView.Style.automatic](./automatic.md)
  The system resolves the table view style based on the table view hierarchy.
- [NSTableView.Style.fullWidth](./fullwidth.md)
  The table view style resolves to a full-width style.
- [NSTableView.Style.inset](./inset.md)
  The table view style resolves to an inset style.
- [NSTableView.Style.plain](./plain.md)
  The table view style resolves to a plain style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/style-swift.enum/sourcelist)*