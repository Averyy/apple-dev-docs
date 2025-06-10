# NSLayoutManager.ControlCharacterAction

**Framework**: AppKit  
**Kind**: struct

Constants that describe actions for control characters.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct ControlCharacterAction
```

#### Overview

These constants [`layoutManager(_:shouldUse:forControlCharacterAt:)`](nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:).md) delegate method uses.

## Topics

### Actions
- [static var containerBreak: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/containerbreak.md)
  An action that triggers a break in layout for the current container.
- [static var horizontalTab: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/horizontaltab.md)
  An action that inserts a horizontal tab.
- [static var lineBreak: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/linebreak.md)
  An action that causes a line break.
- [static var paragraphBreak: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/paragraphbreak.md)
  An action that causes a paragraph break.
- [static var whitespace: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/whitespace.md)
  An action that adds whitespace.
- [static var zeroAdvancement: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/zeroadvancement.md)
  An action that removes the glyph from layout.
### Initializers
- [init(rawValue: Int)](nslayoutmanager/controlcharacteraction/init(rawvalue:).md)
  Creates a new control character action with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:).md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange) -> Int](nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:).md)
  Enables customization of the initial glyph generation process.
- [func layoutManager(NSLayoutManager, shouldUse: NSLayoutManager.ControlCharacterAction, forControlCharacterAt: Int) -> NSLayoutManager.ControlCharacterAction](nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:).md)
  Returns the control character action for the control character at the specified character index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/controlcharacteraction)*