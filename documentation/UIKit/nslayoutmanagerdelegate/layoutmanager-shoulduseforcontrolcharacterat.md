# layoutManager(_:shouldUse:forControlCharacterAt:)

**Framework**: UIKit  
**Kind**: method

Returns the control character action for the control character at the specified character index.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUse action: NSLayoutManager.ControlCharacterAction, forControlCharacterAt charIndex: Int) -> NSLayoutManager.ControlCharacterAction
```

#### Return Value

The control character action for the control character at the given index.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `action`: The proposed control character action for the character at the given index. Possible values are enumerated by   .
- `charIndex`: The index of the control character for which the action is proposed.

## See Also

- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:).md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange) -> Int](nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:).md)
  Enables customization of the initial glyph generation process.
- [NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction.md)
  Constants that describe actions for control characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:))*