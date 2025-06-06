# init(alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance with the given spacing and alignment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init<V>(alignment: Alignment = .center, spacing: CGFloat?, @ViewBuilder content: () -> V) where Content == ZStackContent3D<V>, V : View
```

## Parameters

- `alignment`: The guide for aligning the subviews in this stack on both the x- and y-axes.
- `spacing`: The distance between adjacent subviews, or   if you want the stack to   choose a default distance for each pair of subviews.
- `content`: A view builder that creates the content of this stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zstack/init(alignment:spacing:content:))*