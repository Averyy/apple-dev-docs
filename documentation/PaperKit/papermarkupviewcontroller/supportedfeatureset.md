# supportedFeatureSet

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The supported PaperKit features on this canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
@MainActor
@preconcurrency var supportedFeatureSet: FeatureSet { get }
```

*macOS*

```swift
@MainActor
@preconcurrency final let supportedFeatureSet: FeatureSet
```

## See Also

### Displaying markup
- [var markup: PaperMarkup?](./markup.md)
  The paper data that this view controller displays.
- [var contentView: UIView?](./contentview-4aeda.md)
  The content that markup appears on top of.
- [var contentView: NSView?](./contentview-4hbkf.md)
  The content that markup appears on top of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/supportedfeatureset)*