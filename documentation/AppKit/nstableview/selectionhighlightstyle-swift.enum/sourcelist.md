# NSTableView.SelectionHighlightStyle.sourceList

**Framework**: AppKit  
**Kind**: case

**Availability**:
- macOS 10.5+

## Declaration

```swift
case sourceList
```

#### Discussion

The source list style of NSTableView. On 10.5, a light blue gradient is used to highlight selected rows.

> **Note**:  When using this style, cell subclasses that implement `drawsBackground` must set the value to [`false`](https://developer.apple.com/documentation/swift/false). Otherwise, the cells will draw over the tableview’s highlighting.

 When using this style, cell subclasses that implement `drawsBackground` must set the value to [`false`](https://developer.apple.com/documentation/swift/false). Otherwise, the cells will draw over the tableview’s highlighting.

## See Also

- [NSTableView.SelectionHighlightStyle.none](nstableview/selectionhighlightstyle-swift.enum/none.md)
- [NSTableView.SelectionHighlightStyle.regular](nstableview/selectionhighlightstyle-swift.enum/regular.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectionhighlightstyle-swift.enum/sourcelist)*