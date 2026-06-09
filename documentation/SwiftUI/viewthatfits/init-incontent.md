# init(in:content:)

**Framework**: SwiftUI  
**Kind**: init

Produces a view constrained in the given axes from one of several alternatives provided by a content builder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(in axes: Axis.Set = [.horizontal, .vertical], @ContentBuilder content: () -> Content)
```

## Parameters

- `axes`: A set of axes to constrain children to. The set may contain [`Axis.horizontal`](axis/horizontal.md), [`Axis.vertical`](axis/vertical.md), or both of these. `ViewThatFits` chooses the first child whose size fits within the proposed size on these axes. If `axes` is an empty set, `ViewThatFits` uses the first child view. By default, `ViewThatFits` uses both axes.
- `content`: A content builder that provides the child views for this container, in order of preference. The builder chooses the first child view that fits within the proposed width, height, or both, as defined by `axes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewthatfits/init(in:content:))*