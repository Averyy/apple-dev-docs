# selectedRanges

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns an array of selected ranges.

**Availability**:
- macOS

## Declaration

```swift
optional var selectedRanges: [NSValue] { get set }
```

```objc
@property (copy) NSArray<NSValue *> * selectedRanges;
```

#### Discussion

This property is required for the replace all in selection, select all, and select all in selection actions. The returned `NSArray` object should contain `NSRanges` wrapped by `NSValues`.

## See Also

### Selection Information
- [var isSelectable: Bool](./isselectable.md)
  Returns whether the text is selectable.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  Returns whether multiple items can be selected.
- [var firstSelectedRange: NSRange](./firstselectedrange.md)
  Returns the currently selected range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/selectedranges)*