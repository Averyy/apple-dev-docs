# usesFontLeading

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var usesFontLeading: Bool { get set }
```

#### Discussion

If set to `true`, uses the leading as specified by the font. However, this isn’t appropriate for most UI text. Defaults to `true`.

## See Also

- [var layoutQueue: OperationQueue?](nstextlayoutmanager/layoutqueue.md)
  The queue that the framework dispatches layout operations on.
- [var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)?](nstextlayoutmanager/renderingattributesvalidator.md)
  A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [var usesHyphenation: Bool](nstextlayoutmanager/useshyphenation.md)
  A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.
- [var limitsLayoutForSuspiciousContents: Bool](nstextlayoutmanager/limitslayoutforsuspiciouscontents.md)
  A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/usesfontleading)*