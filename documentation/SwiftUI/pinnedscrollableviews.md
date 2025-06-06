# PinnedScrollableViews

**Framework**: SwiftUI  
**Kind**: struct

A set of view types that may be pinned to the bounds of a scroll view.

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
struct PinnedScrollableViews
```

## Mentions

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)

## Topics

### Getting scrollable view types
- [static let sectionHeaders: PinnedScrollableViews](pinnedscrollableviews/sectionheaders.md)
  The header view of each `Section` will be pinned.
- [static let sectionFooters: PinnedScrollableViews](pinnedscrollableviews/sectionfooters.md)
  The footer view of each `Section` will be pinned.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
  Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
  Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [struct LazyHStack](lazyhstack.md)
  A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [struct LazyVStack](lazyvstack.md)
  A view that arranges its children in a line that grows vertically, creating items only as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pinnedscrollableviews)*