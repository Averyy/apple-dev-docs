# layoutQueue

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The queue that the framework dispatches layout operations on.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var layoutQueue: OperationQueue? { get set }
```

```objc
@property (strong, nullable) NSOperationQueue * layoutQueue;
```

#### Discussion

If non-`nil`, it performs layout in the specified queue until `estimatedUsageBounds` becomes `false`.

## See Also

### Configuring global layout manager options
- [var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)?](./renderingattributesvalidator.md)
  A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [var usesHyphenation: Bool](./useshyphenation.md)
  A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.
- [var limitsLayoutForSuspiciousContents: Bool](./limitslayoutforsuspiciouscontents.md)
  A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/layoutqueue)*