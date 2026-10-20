# selection

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The current selected elements on the canvas.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency var selection: Set<MarkupOrderedSet.ElementID> { get set }
```

## See Also

### Selecting elements
- [var selectedMarkup: PaperMarkup](./selectedmarkup.md)
  The selected contents in the UI.
- [func suggestedFrameForInserting(contentInFrame: CGRect) -> CGRect](./suggestedframeforinserting%28contentinframe%29.md)
  Returns the suggested frame for inserting shapes and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/selection)*