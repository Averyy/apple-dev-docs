# layoutManager(_:shouldUse:forControlCharacterAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the control character action for the control character at the specified character index.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUse action: NSLayoutManager.ControlCharacterAction, forControlCharacterAt charIndex: Int) -> NSLayoutManager.ControlCharacterAction
```

```objc
- (NSControlCharacterAction) layoutManager:(NSLayoutManager *) layoutManager shouldUseAction:(NSControlCharacterAction) action forControlCharacterAtIndex:(NSUInteger) charIndex;
```

## Return Value

The control character action for the control character at the given index.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `action`: The proposed control character action for the character at the given index. Possible values are enumerated by [`NSLayoutManager.ControlCharacterAction`](../nslayoutmanager/controlcharacteraction.md).
- `charIndex`: The index of the control character for which the action is proposed.

## See Also

### Invalidating glyphs and layout
- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](./layoutmanagerdidinvalidatelayout%28_%29.md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange) -> Int](./layoutmanager%28_,shouldgenerateglyphs,properties,characterindexes,font,forglyphrange%29.md)
  Enables customization of the initial glyph generation process.
- [NSLayoutManager.ControlCharacterAction](../nslayoutmanager/controlcharacteraction.md)
  Constants that describe actions for control characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:))*