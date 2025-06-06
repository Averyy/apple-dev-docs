# firstSelectedRange

**Framework**: AppKit  
**Kind**: property

Returns the currently selected range.

**Availability**:
- macOS ?+

## Declaration

```swift
optional var firstSelectedRange: NSRange { get }
```

#### Discussion

This property is required for the next match, previous match, replace, replace and find and set search string actions. The client should return its first selected range, or {index, 0} to indicate the location of the insertion point if there is no selection.

## See Also

- [var isSelectable: Bool](nstextfinderclient/isselectable.md)
  Returns whether the text is selectable.
- [var allowsMultipleSelection: Bool](nstextfinderclient/allowsmultipleselection.md)
  Returns whether multiple items can be selected.
- [var selectedRanges: [NSValue]](nstextfinderclient/selectedranges.md)
  Returns an array of selected ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/firstselectedrange)*