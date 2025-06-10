# webViewScrollPosition(_:)

**Framework**: SwiftUI  
**Kind**: method

Associates a binding to a scroll position with the web view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func webViewScrollPosition(_ position: Binding<ScrollPosition>) -> some View
```

#### Discussion

> **Note**: `WebView` does not support scrolling to a view with an identity. It only supports scrolling to a concrete offset, or to an edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewscrollposition(_:))*