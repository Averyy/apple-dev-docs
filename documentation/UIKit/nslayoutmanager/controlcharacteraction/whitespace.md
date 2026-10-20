# whitespace

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An action that adds whitespace.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var whitespace: NSLayoutManager.ControlCharacterAction { get }
```

```c
NSControlCharacterActionWhitespace
```

#### Discussion

The width for a glyph with this action is determined by the delegate method [`layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](../../nslayoutmanagerdelegate/layoutmanager%28_,boundingboxforcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md) if the method is implemented; otherwise, same as `NSControlCharacterZeroAdvancementAction`.

## See Also

### Actions
- [static var containerBreak: NSLayoutManager.ControlCharacterAction](./containerbreak.md)
  An action that triggers a break in layout for the current container.
- [static var horizontalTab: NSLayoutManager.ControlCharacterAction](./horizontaltab.md)
  An action that inserts a horizontal tab.
- [static var lineBreak: NSLayoutManager.ControlCharacterAction](./linebreak.md)
  An action that causes a line break.
- [static var paragraphBreak: NSLayoutManager.ControlCharacterAction](./paragraphbreak.md)
  An action that causes a paragraph break.
- [static var zeroAdvancement: NSLayoutManager.ControlCharacterAction](./zeroadvancement.md)
  An action that removes the glyph from layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/whitespace)*