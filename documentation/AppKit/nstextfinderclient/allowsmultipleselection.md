# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property

Returns whether multiple items can be selected.

**Availability**:
- macOS ?+

## Declaration

```swift
optional var allowsMultipleSelection: Bool { get }
```

#### Discussion

If this properties is not implemented, the text finder will act as if they returned [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var isSelectable: Bool](nstextfinderclient/isselectable.md)
  Returns whether the text is selectable.
- [var firstSelectedRange: NSRange](nstextfinderclient/firstselectedrange.md)
  Returns the currently selected range.
- [var selectedRanges: [NSValue]](nstextfinderclient/selectedranges.md)
  Returns an array of selected ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/allowsmultipleselection)*