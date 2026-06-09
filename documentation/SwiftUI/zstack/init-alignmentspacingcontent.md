# init(alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance with the given spacing and alignment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
init<V>(alignment: Alignment = .center, spacing: CGFloat?, @ContentBuilder content: () -> V) where Content == ZStackContent3D<V>, V : View
```

## Parameters

- `alignment`: The guide for aligning the subviews in this stack on both the x- and y-axes.
- `spacing`: The distance between adjacent subviews, or `nil` if you want the stack to choose a default distance for each pair of subviews.
- `content`: A content builder that creates the content of this stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zstack/init(alignment:spacing:content:))*