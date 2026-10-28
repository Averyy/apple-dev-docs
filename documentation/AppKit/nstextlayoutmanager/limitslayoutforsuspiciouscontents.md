# limitsLayoutForSuspiciousContents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var limitsLayoutForSuspiciousContents: Bool { get set }
```

```objc
@property BOOL limitsLayoutForSuspiciousContents;
```

## Discussion

By enabling this functionality, it’s possible that certain text — such as a very long paragraph — might result in an unexpected layout. Defaults to `false`.

## See Also

### Configuring global layout manager options
- [var layoutQueue: OperationQueue?](./layoutqueue.md)
  The queue that the framework dispatches layout operations on.
- [var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)?](./renderingattributesvalidator.md)
  A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [var usesHyphenation: Bool](./useshyphenation.md)
  A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/limitslayoutforsuspiciouscontents)*