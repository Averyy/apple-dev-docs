# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns whether multiple items can be selected.

**Availability**:
- macOS

## Declaration

```swift
optional var allowsMultipleSelection: Bool { get }
```

```objc
@property (readonly) BOOL allowsMultipleSelection;
```

#### Discussion

If this properties is not implemented, the text finder will act as if they returned [`true`](../../Swift/true.md).

## See Also

### Selection Information
- [var isSelectable: Bool](./isselectable.md)
  Returns whether the text is selectable.
- [var firstSelectedRange: NSRange](./firstselectedrange.md)
  Returns the currently selected range.
- [var selectedRanges: [NSValue]](./selectedranges.md)
  Returns an array of selected ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/allowsmultipleselection)*