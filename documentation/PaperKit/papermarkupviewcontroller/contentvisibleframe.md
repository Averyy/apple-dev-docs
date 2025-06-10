# contentVisibleFrame

**Framework**: PaperKit  
**Kind**: property

The visible area of content in the scroll view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var contentVisibleFrame: CGRect { get set }
```

#### Discussion

Modifying this property immediately moves the canvas, to animate changing the visible rect use [`setContentVisibleFrame(_:animated:)`](papermarkupviewcontroller/setcontentvisibleframe(_:animated:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/contentvisibleframe)*