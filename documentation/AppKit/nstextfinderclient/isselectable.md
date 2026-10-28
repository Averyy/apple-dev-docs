# isSelectable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns whether the text is selectable.

**Availability**:
- macOS

## Declaration

```swift
optional var isSelectable: Bool { get }
```

```objc
@property (readonly, getter=isSelectable) BOOL selectable;
```

## Discussion

If this properties is not implemented, the text finder will act as if they returned [`true`](../../Swift/true.md).

## See Also

### Selection Information
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  Returns whether multiple items can be selected.
- [var firstSelectedRange: NSRange](./firstselectedrange.md)
  Returns the currently selected range.
- [var selectedRanges: [NSValue]](./selectedranges.md)
  Returns an array of selected ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/isselectable)*