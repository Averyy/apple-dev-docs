# firstSelectedRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the currently selected range.

**Availability**:
- macOS

## Declaration

```swift
optional var firstSelectedRange: NSRange { get }
```

```objc
@property (readonly) NSRange firstSelectedRange;
```

#### Discussion

This property is required for the next match, previous match, replace, replace and find and set search string actions. The client should return its first selected range, or {index, 0} to indicate the location of the insertion point if there is no selection.

## See Also

### Selection Information
- [var isSelectable: Bool](./isselectable.md)
  Returns whether the text is selectable.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  Returns whether multiple items can be selected.
- [var selectedRanges: [NSValue]](./selectedranges.md)
  Returns an array of selected ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/firstselectedrange)*