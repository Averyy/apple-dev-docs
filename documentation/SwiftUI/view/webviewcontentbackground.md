# webViewContentBackground(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the visibility of the webpage’s natural background color within this view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func webViewContentBackground(_ visibility: Visibility) -> some View
```

#### Discussion

By default, WebViews are opaque, and use the page’s natural background color as their background color. Use this modifier if you would like to not use this behavior and instead provide a custom background using SwiftUI.

## Parameters

- `visibility`: The visibility to use for the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewcontentbackground(_:))*