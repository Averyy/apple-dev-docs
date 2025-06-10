# setContentVisibleFrame(_:animated:)

**Framework**: PaperKit  
**Kind**: method

Zooms to a specific area of the content so that it’s visible in the scroll view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func setContentVisibleFrame(_ rect: CGRect, animated: Bool)
```

#### Discussion

- rect: A rectangle defining an area of the content view. The rectangle should be in the coordinate space of the data model.
- animated: `true` if the scrolling should be animated, `false` if it should be immediate.

This method scrolls the content so that the area defined by rect is just visible. If the area is already visible, the method does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/setcontentvisibleframe(_:animated:))*