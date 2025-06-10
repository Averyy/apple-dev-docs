# webViewOnScrollGeometryChange(for:of:action:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to be performed when a value, created from a scroll geometry, changes.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func webViewOnScrollGeometryChange<T>(for type: T.Type, of transform: @escaping (ScrollGeometry) -> T, action: @escaping (T, T) -> Void) -> some View where T : Hashable
```

#### Discussion

> **Note**: The content size of web content may exceed the current size of the view’s frame, however it will never be smaller than it.

## Parameters

- `type`: The type of value transformed from a  .
- `transform`: A closure that transforms a   to your type.
- `action`: A closure to run when the transformed data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/webviewonscrollgeometrychange(for:of:action:))*