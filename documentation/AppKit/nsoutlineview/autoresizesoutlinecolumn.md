# autoresizesOutlineColumn

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the outline view resizes its outline column when the user expands or collapses items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autoresizesOutlineColumn: Bool { get set }
```

#### Discussion

The outline column contains the cells with the expansion symbols and is generally the first column. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which causes the outline column to be resized.

The outline column is resized based on how many indentation levels are exposed or hidden. For example, if expanding a row exposes a single indentation level, the outline column width is increased by one [`indentationPerLevel`](nsoutlineview/indentationperlevel.md).

## See Also

- [var outlineTableColumn: NSTableColumn?](nsoutlineview/outlinetablecolumn.md)
  The table column in which hierarchical data is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/autoresizesoutlinecolumn)*