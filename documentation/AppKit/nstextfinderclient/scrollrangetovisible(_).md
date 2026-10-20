# scrollRangeToVisible(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the specified range such that it is visible.

**Availability**:
- macOS

## Declaration

```swift
optional func scrollRangeToVisible(_ range: NSRange)
```

```objc
- (void) scrollRangeToVisible:(NSRange) range;
```

#### Discussion

This method is used by all actions, but is not strictly required by any.

## Parameters

- `range`: The range to display.

## See Also

### Determining and Displaying Text Locations
- [func contentView(at: Int, effectiveCharacterRange: NSRangePointer) -> NSView](./contentview%28at,effectivecharacterrange%29.md)
  Returns the view the context is displayed in.
- [func rects(forCharacterRange: NSRange) -> [NSValue]?](./rects%28forcharacterrange%29.md)
  An array containing the located text in the content view’s coordinate system.
- [var visibleCharacterRanges: [NSValue]](./visiblecharacterranges.md)
  An array of visible character ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/scrollrangetovisible(_:))*