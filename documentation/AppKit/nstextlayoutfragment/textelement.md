# textElement

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The parent text element.

**Availability**:
- macOS 12.0+

## Declaration

```swift
weak var textElement: NSTextElement? { get }
```

```objc
@property (weak, readonly) NSTextElement * textElement;
```

## See Also

### Getting element information
- [var state: NSTextLayoutFragment.State](./state-swift.property.md)
  The layout information state.
- [NSTextLayoutFragment.State](./state-swift.enum.md)
  Values that describe the possible layout states.
- [var rangeInElement: NSTextRange](./rangeinelement.md)
  The range inside the text element relative to the document origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/textelement)*