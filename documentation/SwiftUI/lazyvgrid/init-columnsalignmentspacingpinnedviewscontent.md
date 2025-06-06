# init(columns:alignment:spacing:pinnedViews:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a grid that grows vertically.

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
init(columns: [GridItem], alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, pinnedViews: PinnedScrollableViews = .init(), @ViewBuilder content: () -> Content)
```

## Parameters

- `columns`: An array of grid items to size and position each row of   the grid.
- `alignment`: The alignment of the grid within its parent view.
- `spacing`: The spacing between the grid and the next item in its   parent view.
- `pinnedViews`: Views to pin to the bounds of a parent scroll view.
- `content`: The content of the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazyvgrid/init(columns:alignment:spacing:pinnedviews:content:))*