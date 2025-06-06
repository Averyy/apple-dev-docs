# outlineTableColumn

**Framework**: AppKit  
**Kind**: property

The table column in which hierarchical data is displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var outlineTableColumn: NSTableColumn? { get set }
```

#### Discussion

Each level of hierarchical data is indented by the amount specified by the [`indentationPerLevel`](nsoutlineview/indentationperlevel.md) property (the default is `16.0`), and decorated with the indentation marker (disclosure triangle) on rows that are expandable. Outline table column data is archived with the rest of the outline view’s state information.

Attempts to set the value of this property to `nil` are silently ignored.

## See Also

- [var autoresizesOutlineColumn: Bool](nsoutlineview/autoresizesoutlinecolumn.md)
  A Boolean value that indicates whether the outline view resizes its outline column when the user expands or collapses items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/outlinetablecolumn)*