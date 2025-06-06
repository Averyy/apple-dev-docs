# scrollRangeToVisible(_:)

**Framework**: AppKit  
**Kind**: method

Scrolls the specified range such that it is visible.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func scrollRangeToVisible(_ range: NSRange)
```

#### Discussion

This method is used by all actions, but is not strictly required by any.

## Parameters

- `range`: The range to display.

## See Also

- [func contentView(at: Int, effectiveCharacterRange: NSRangePointer) -> NSView](nstextfinderclient/contentview(at:effectivecharacterrange:).md)
  Returns the view the context is displayed in.
- [func rects(forCharacterRange: NSRange) -> [NSValue]?](nstextfinderclient/rects(forcharacterrange:).md)
  An array containing the located text in the content view’s coordinate system.
- [var visibleCharacterRanges: [NSValue]](nstextfinderclient/visiblecharacterranges.md)
  An array of visible character ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/scrollrangetovisible(_:))*