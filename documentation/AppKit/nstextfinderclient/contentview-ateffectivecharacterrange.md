# contentView(at:effectiveCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Returns the view the context is displayed in.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func contentView(at index: Int, effectiveCharacterRange outRange: NSRangePointer) -> NSView
```

#### Return Value

Returns the view the contains the found text.

## Parameters

- `index`: The index of the view containing the located text.
- `outRange`: Returns, by reference, the entire range of the string displayed by the view

## See Also

- [func rects(forCharacterRange: NSRange) -> [NSValue]?](nstextfinderclient/rects(forcharacterrange:).md)
  An array containing the located text in the content view’s coordinate system.
- [func scrollRangeToVisible(NSRange)](nstextfinderclient/scrollrangetovisible(_:).md)
  Scrolls the specified range such that it is visible.
- [var visibleCharacterRanges: [NSValue]](nstextfinderclient/visiblecharacterranges.md)
  An array of visible character ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/contentview(at:effectivecharacterrange:))*