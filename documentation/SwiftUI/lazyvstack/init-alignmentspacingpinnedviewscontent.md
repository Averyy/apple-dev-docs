# init(alignment:spacing:pinnedViews:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a lazy vertical stack view with the given spacing, vertical alignment, pinning behavior, and content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, pinnedViews: PinnedScrollableViews = .init(), @ViewBuilder content: () -> Content)
```

## Parameters

- `alignment`: The guide for aligning the subviews in this stack. All   child views have the same horizontal screen coordinate.
- `spacing`: The distance between adjacent subviews, or   if you   want the stack to choose a default distance for each pair of   subviews.
- `pinnedViews`: The kinds of child views that will be pinned.
- `content`: A view builder that creates the content of this stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazyvstack/init(alignment:spacing:pinnedviews:content:))*