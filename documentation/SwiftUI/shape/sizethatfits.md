# sizeThatFits(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Returns the size of the view that will render the shape, given a proposed size.

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
func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

#### Return Value

A size that indicates how much space the shape needs.

#### Discussion

Implement this method to tell the container of the shape how much space the shape needs to render itself, given a size proposal.

See [`sizeThatFits(proposal:subviews:cache:)`](layout/sizethatfits(proposal:subviews:cache:).md) for more details about how the layout system chooses the size of views.

## Parameters

- `proposal`: A size proposal for the container.

## See Also

- [func path(in: CGRect) -> Path](shape/path(in:).md)
  Describes this shape as a path within a rectangular frame of reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/sizethatfits(_:))*