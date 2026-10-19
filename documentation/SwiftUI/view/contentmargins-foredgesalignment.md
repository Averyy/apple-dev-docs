# contentMargins(for:edges:alignment:)

**Framework**: SwiftUI  
**Kind**: method

Insets the content of this view by a content margin guide.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
nonisolated
func contentMargins(for guide: ContentMarginGuide, edges: Edge.Set = .all, alignment: Alignment? = nil) -> some View
```

#### Return Value

A view inset on `edges` by `guide`.

#### Discussion

Use this modifier to lay a view out against a system metric, like the margins of the container it appears in:

```swift
NavigationStack {
    AlbumGrid()
        .contentMargins(for: .container, edges: .horizontal)
}
```

The view is proposed the size it would otherwise receive, and is inset by the value of `guide` when it’s placed.

A view that doesn’t fill the size it was proposed is positioned within the inset bounds using `alignment`. Here, a compose button sits in the bottom trailing corner of the margins of its container:

```swift
ZStack {
    MessageList()
    ComposeButton()
        .contentMargins(
            for: .container, alignment: .bottomTrailing)
}
```

## Parameters

- `guide`: The guide that provides the insets.
- `edges`: The edges to inset, any edges not in this set are unchanged, even when `guide` provides a value for them.
- `alignment`: The alignment of the view within the inset bounds. Most alignment values have no apparent effect when the view fills the size it was proposed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contentmargins(for:edges:alignment:))*