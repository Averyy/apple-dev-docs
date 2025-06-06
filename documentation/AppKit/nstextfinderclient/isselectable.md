# isSelectable

**Framework**: AppKit  
**Kind**: property

Returns whether the text is selectable.

**Availability**:
- macOS ?+

## Declaration

```swift
optional var isSelectable: Bool { get }
```

#### Discussion

If this properties is not implemented, the text finder will act as if they returned [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var allowsMultipleSelection: Bool](nstextfinderclient/allowsmultipleselection.md)
  Returns whether multiple items can be selected.
- [var firstSelectedRange: NSRange](nstextfinderclient/firstselectedrange.md)
  Returns the currently selected range.
- [var selectedRanges: [NSValue]](nstextfinderclient/selectedranges.md)
  Returns an array of selected ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/isselectable)*