# contentMargins(for:edges:)

**Framework**: SwiftUI  
**Kind**: method

The insets of a content margin guide for the given edges.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
func contentMargins(for guide: ContentMarginGuide, edges: Edge.Set = .all) -> EdgeInsets
```

#### Return Value

The insets `guide` provides for `edges`. Edges not in the set have a value of zero.

#### Discussion

Read a guide when you need its value rather than the inset, like a view that draws its own content:

```swift
GeometryReader { proxy in
    Canvas { context, size in
        drawChart(
            in: context, size: size,
            insets: proxy.contentMargins(for: .container, edges: .horizontal))
    }
}
```

## Parameters

- `guide`: The guide that provides the insets.
- `edges`: The edges to read insets for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/contentmargins(for:edges:))*