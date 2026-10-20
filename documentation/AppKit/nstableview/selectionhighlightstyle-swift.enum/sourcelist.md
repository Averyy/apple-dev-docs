# NSTableView.SelectionHighlightStyle.sourceList

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

**Availability**:
- macOS 10.5+ - Deprecated in 12.0

> **Deprecated**: Set the NSTableView.style property to NSTableViewStyleSourceList instead.

## Declaration

```swift
case sourceList
```

```c
NSTableViewSelectionHighlightStyleSourceList
```

#### Discussion

The source list style of NSTableView. On 10.5, a light blue gradient is used to highlight selected rows.

> **Note**:  When using this style, cell subclasses that implement `drawsBackground` must set the value to [`false`](../../../Swift/false.md). Otherwise, the cells will draw over the tableview’s highlighting.

## See Also

### Constants
- [NSTableView.SelectionHighlightStyle.none](./none.md)
- [NSTableView.SelectionHighlightStyle.regular](./regular.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectionhighlightstyle-swift.enum/sourcelist)*