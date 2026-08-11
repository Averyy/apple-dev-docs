# selection

**Framework**: PaperKit  
**Kind**: property

The current selected elements on the canvas.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var selection: Set<MarkupOrderedSet.ElementID> { get set }
```

## See Also

- [var selectedMarkup: PaperMarkup](papermarkupviewcontroller/selectedmarkup.md)
  The selected contents in the UI.
- [func suggestedFrameForInserting(contentInFrame: CGRect) -> CGRect](papermarkupviewcontroller/suggestedframeforinserting(contentinframe:).md)
  Returns the suggested frame for inserting shapes and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/selection)*