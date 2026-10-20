# rects(forCharacterRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An array containing the located text in the content view’s coordinate system.

**Availability**:
- macOS

## Declaration

```swift
optional func rects(forCharacterRange range: NSRange) -> [NSValue]?
```

```objc
- (NSArray<NSValue *> *) rectsForCharacterRange:(NSRange) range;
```

#### Return Value

An array containing the rectangles containing the located text in the content view object’s coordinate system and return that array. The rectangles are return wrapped as `NSValue` objects.

#### Discussion

The text finder uses this method to determine the location to display the find indicator.

The given range is guaranteed not to overlap multiple views.

## Parameters

- `range`: The range of the located character string.

## See Also

### Determining and Displaying Text Locations
- [func contentView(at: Int, effectiveCharacterRange: NSRangePointer) -> NSView](./contentview%28at,effectivecharacterrange%29.md)
  Returns the view the context is displayed in.
- [func scrollRangeToVisible(NSRange)](./scrollrangetovisible%28_%29.md)
  Scrolls the specified range such that it is visible.
- [var visibleCharacterRanges: [NSValue]](./visiblecharacterranges.md)
  An array of visible character ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/rects(forcharacterrange:))*