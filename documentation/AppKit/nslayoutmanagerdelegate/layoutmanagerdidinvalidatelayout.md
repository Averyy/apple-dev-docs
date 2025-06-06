# layoutManagerDidInvalidateLayout(_:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate when the specified layout manager invalidates layout information (not glyph information).

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func layoutManagerDidInvalidateLayout(_ sender: NSLayoutManager)
```

#### Discussion

This method is invoked only when layout was complete and then became invalidated for some reason. Delegates can use this information to show an indicator of background layout or to enable a button that forces immediate layout of text.

## Parameters

- `sender`: The layout manager that invalidated layout.

## See Also

- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange) -> Int](nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:).md)
  Enables customization of the initial glyph generation process.
- [func layoutManager(NSLayoutManager, shouldUse: NSLayoutManager.ControlCharacterAction, forControlCharacterAt: Int) -> NSLayoutManager.ControlCharacterAction](nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:).md)
  Returns the control character action for the control character at the specified character index.
- [NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction.md)
  Constants that describe actions for control characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:))*