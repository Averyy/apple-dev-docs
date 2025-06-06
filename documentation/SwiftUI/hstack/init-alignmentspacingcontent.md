# init(alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a horizontal stack with the given spacing and vertical alignment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> Content)
```

## Parameters

- `alignment`: The guide for aligning the subviews in this stack. This   guide has the same vertical screen coordinate for every subview.
- `spacing`: The distance between adjacent subviews, or   if you   want the stack to choose a default distance for each pair of   subviews.
- `content`: A view builder that creates the content of this stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hstack/init(alignment:spacing:content:))*