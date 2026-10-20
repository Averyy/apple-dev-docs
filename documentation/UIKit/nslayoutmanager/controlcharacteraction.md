# NSLayoutManager.ControlCharacterAction

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that describe actions for control characters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct ControlCharacterAction
```

```c
enum NSControlCharacterAction : NSInteger;
```

#### Overview

These constants [`layoutManager(_:shouldUse:forControlCharacterAt:)`](../nslayoutmanagerdelegate/layoutmanager%28_,shoulduse,forcontrolcharacterat%29.md) delegate method uses.

## Topics

### Actions
- [static var containerBreak: NSLayoutManager.ControlCharacterAction](./controlcharacteraction/containerbreak.md)
  An action that triggers a break in layout for the current container.
- [static var horizontalTab: NSLayoutManager.ControlCharacterAction](./controlcharacteraction/horizontaltab.md)
  An action that inserts a horizontal tab.
- [static var lineBreak: NSLayoutManager.ControlCharacterAction](./controlcharacteraction/linebreak.md)
  An action that causes a line break.
- [static var paragraphBreak: NSLayoutManager.ControlCharacterAction](./controlcharacteraction/paragraphbreak.md)
  An action that causes a paragraph break.
- [static var whitespace: NSLayoutManager.ControlCharacterAction](./controlcharacteraction/whitespace.md)
  An action that adds whitespace.
- [static var zeroAdvancement: NSLayoutManager.ControlCharacterAction](./controlcharacteraction/zeroadvancement.md)
  An action that removes the glyph from layout.
### Initializers
- [init(rawValue: Int)](./controlcharacteraction/init%28rawvalue%29.md)
  Creates a new control character action with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Invalidating glyphs and layout
- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](../nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout%28_%29.md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange) -> Int](../nslayoutmanagerdelegate/layoutmanager%28_,shouldgenerateglyphs,properties,characterindexes,font,forglyphrange%29.md)
  Enables customization of the initial glyph generation process.
- [func layoutManager(NSLayoutManager, shouldUse: NSLayoutManager.ControlCharacterAction, forControlCharacterAt: Int) -> NSLayoutManager.ControlCharacterAction](../nslayoutmanagerdelegate/layoutmanager%28_,shoulduse,forcontrolcharacterat%29.md)
  Returns the control character action for the control character at the specified character index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction)*