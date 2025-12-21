# LazyVStack

**Framework**: SwiftUI  
**Kind**: struct

A view that arranges its children in a line that grows vertically, creating items only as needed.

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
struct LazyVStack<Content> where Content : View
```

## Mentions

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Displaying data in lists](displaying-data-in-lists.md)

#### Overview

The stack is “lazy,” in that the stack view doesn’t create items until it needs to render them onscreen.

In the following example, a [`ScrollView`](scrollview.md) contains a `LazyVStack` that consists of a vertical row of text views. The stack aligns to the leading edge of the scroll view, and uses default spacing between the text views.

```swift
ScrollView {
    LazyVStack(alignment: .leading) {
        ForEach(1...100, id: \.self) {
            Text("Row \($0)")
        }
    }
}
```

## Topics

### Creating a lazy-loading vertical stack
- [init(alignment: HorizontalAlignment, spacing: CGFloat?, pinnedViews: PinnedScrollableViews, content: () -> Content)](lazyvstack/init(alignment:spacing:pinnedviews:content:).md)
  Creates a lazy vertical stack view with the given spacing, vertical alignment, pinning behavior, and content.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
  Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
  Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [struct LazyHStack](lazyhstack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct PinnedScrollableViews](pinnedscrollableviews.md)
  A set of view types that may be pinned to the bounds of a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazyvstack)*