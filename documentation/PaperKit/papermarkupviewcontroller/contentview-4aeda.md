# contentView

**Framework**: PaperKit  
**Kind**: property

The content that markup appears on top of.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var contentView: UIView? { get set }
```

#### Discussion

The system sizes the content view to the frame of the markup and adds it below all the markup and drawing. When `nil`, markup appears on top of a blank white canvas.

Default is `nil`.

## See Also

- [var markup: PaperMarkup?](papermarkupviewcontroller/markup.md)
  The paper data that this view controller displays.
- [var contentView: NSView?](papermarkupviewcontroller/contentview-4hbkf.md)
  The content that markup appears on top of.
- [var supportedFeatureSet: FeatureSet](papermarkupviewcontroller/supportedfeatureset.md)
  The supported PaperKit features on this canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/contentview-4aeda)*