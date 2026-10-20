# renderingAttributesValidator

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^renderingAttributesValidator)(NSTextLayoutManager *textLayoutManager, NSTextLayoutFragment *textLayoutFragment);
```

#### Discussion

The validator uses [`setRenderingAttributes(_:for:)`](./setrenderingattributes%28_,for%29.md) to fill the rendering attributes appropriate for the range inside `textLayoutFragment`.

## See Also

### Configuring global layout manager options
- [var layoutQueue: OperationQueue?](./layoutqueue.md)
  The queue that the framework dispatches layout operations on.
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [var usesHyphenation: Bool](./useshyphenation.md)
  A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.
- [var limitsLayoutForSuspiciousContents: Bool](./limitslayoutforsuspiciouscontents.md)
  A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/renderingattributesvalidator)*