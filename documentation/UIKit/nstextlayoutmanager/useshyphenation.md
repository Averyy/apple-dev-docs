# usesHyphenation

**Framework**: UIKit  
**Kind**: property

A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var usesHyphenation: Bool { get set }
```

#### Discussion

Defaults to `true`.

## See Also

- [var layoutQueue: OperationQueue?](nstextlayoutmanager/layoutqueue.md)
  The queue that the framework dispatches layout operations on.
- [var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)?](nstextlayoutmanager/renderingattributesvalidator.md)
  A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [var usesFontLeading: Bool](nstextlayoutmanager/usesfontleading.md)
  A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [var limitsLayoutForSuspiciousContents: Bool](nstextlayoutmanager/limitslayoutforsuspiciouscontents.md)
  A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/useshyphenation)*