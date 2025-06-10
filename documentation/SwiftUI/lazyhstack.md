# LazyHStack

**Framework**: SwiftUI  
**Kind**: struct

A view that arranges its children in a line that grows horizontally, creating items only as needed.

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
struct LazyHStack<Content> where Content : View
```

## Mentions

- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)

#### Overview

The stack is “lazy,” in that the stack view doesn’t create items until it needs to render them onscreen.

In the following example, a [`ScrollView`](scrollview.md) contains a `LazyHStack` that consists of a horizontal row of text views. The stack aligns to the top of the scroll view and uses 10-point spacing between each text view.

```swift
ScrollView(.horizontal) {
    LazyHStack(alignment: .top, spacing: 10) {
        ForEach(1...100, id: \.self) {
            Text("Column \($0)")
        }
    }
}
```

## Topics

### Creating a lazy-loading horizontal stack
- [init(alignment: VerticalAlignment, spacing: CGFloat?, pinnedViews: PinnedScrollableViews, content: () -> Content)](lazyhstack/init(alignment:spacing:pinnedviews:content:).md)
  Creates a lazy horizontal stack view with the given spacing, vertical alignment, pinning behavior, and content.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
  Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
  Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [struct LazyVStack](lazyvstack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.
- [struct PinnedScrollableViews](pinnedscrollableviews.md)
  A set of view types that may be pinned to the bounds of a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazyhstack)*