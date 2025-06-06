# NSTableView.Style.automatic

**Framework**: Appkit  
**Kind**: case

The system resolves the table view style based on the table view hierarchy.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case automatic
```

#### Discussion

The system resolves the table view style in the following manner:

- If the table view is in a sidebar split-view controller item, [`effectiveStyle`](nstableview/effectivestyle.md) resolves to [`NSTableView.Style.sourceList`](nstableview/style-swift.enum/sourcelist.md).
- If the table’s scroll view has a border, [`effectiveStyle`](nstableview/effectivestyle.md) resolves to [`NSTableView.Style.fullWidth`](nstableview/style-swift.enum/fullwidth.md).
- Otherwise, [`effectiveStyle`](nstableview/effectivestyle.md) resolves to [`NSTableView.Style.inset`](nstableview/style-swift.enum/inset.md). However, if the table needs extra space to fit its column cells, [`effectiveStyle`](nstableview/effectivestyle.md) resolves to [`NSTableView.Style.fullWidth`](nstableview/style-swift.enum/fullwidth.md).

> **Note**:  For backward compatibility reasons, when [`selectionHighlightStyle`](nstableview/selectionhighlightstyle-swift.property.md) is [`NSTableView.SelectionHighlightStyle.sourceList`](nstableview/selectionhighlightstyle-swift.enum/sourcelist.md), [`style`](nstableview/style-swift.property.md) also resolves to [`NSTableView.Style.sourceList`](nstableview/style-swift.enum/sourcelist.md).

## See Also

- [NSTableView.Style.fullWidth](nstableview/style-swift.enum/fullwidth.md)
  The table view style resolves to a full-width style.
- [NSTableView.Style.inset](nstableview/style-swift.enum/inset.md)
  The table view style resolves to an inset style.
- [NSTableView.Style.sourceList](nstableview/style-swift.enum/sourcelist.md)
  The table view style resolves to a source-list style.
- [NSTableView.Style.plain](nstableview/style-swift.enum/plain.md)
  The table view style resolves to a plain style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nstableview/style-swift.enum/automatic)*