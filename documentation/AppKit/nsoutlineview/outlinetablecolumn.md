# outlineTableColumn

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The table column in which hierarchical data is displayed.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var outlineTableColumn: NSTableColumn? { get set }
```

```objc
@property (assign, nullable) NSTableColumn * outlineTableColumn;
```

## Discussion

Each level of hierarchical data is indented by the amount specified by the [`indentationPerLevel`](./indentationperlevel.md) property (the default is `16.0`), and decorated with the indentation marker (disclosure triangle) on rows that are expandable. Outline table column data is archived with the rest of the outline view’s state information.

Attempts to set the value of this property to `nil` are silently ignored.

## See Also

### Working with the Outline Column
- [var autoresizesOutlineColumn: Bool](./autoresizesoutlinecolumn.md)
  A Boolean value that indicates whether the outline view resizes its outline column when the user expands or collapses items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/outlinetablecolumn)*