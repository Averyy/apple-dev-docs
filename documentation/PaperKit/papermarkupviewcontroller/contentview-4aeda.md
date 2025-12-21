# contentView

**Framework**: PaperKit  
**Kind**: property

The content that markup happens on top of.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var contentView: UIView? { get set }
```

#### Discussion

The content view is sized to the frame of the `markup`, and added below all the markup and drawing. If this is `nil` then the markup happens on top of a blank white canvas.

Default is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/contentview-4aeda)*