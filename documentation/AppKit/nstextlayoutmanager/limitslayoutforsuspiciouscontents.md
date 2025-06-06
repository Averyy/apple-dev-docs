# limitsLayoutForSuspiciousContents

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var limitsLayoutForSuspiciousContents: Bool { get set }
```

#### Discussion

By enabling this functionality, it’s possible that certain text — such as a very long paragraph — might result in an unexpected layout. Defaults to `false`.

## See Also

- [var layoutQueue: OperationQueue?](nstextlayoutmanager/layoutqueue.md)
  The queue that the framework dispatches layout operations on.
- [var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)?](nstextlayoutmanager/renderingattributesvalidator.md)
  A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [var usesFontLeading: Bool](nstextlayoutmanager/usesfontleading.md)
  A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [var usesHyphenation: Bool](nstextlayoutmanager/useshyphenation.md)
  A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/limitslayoutforsuspiciouscontents)*