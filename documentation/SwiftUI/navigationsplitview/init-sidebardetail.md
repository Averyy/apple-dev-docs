# init(sidebar:detail:)

**Framework**: SwiftUI  
**Kind**: init

Creates a two-column navigation split view.

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
init(@ViewBuilder sidebar: () -> Sidebar, @ViewBuilder detail: () -> Detail) where Content == EmptyView
```

## Mentions

- [Migrating to new navigation types](migrating-to-new-navigation-types.md)

## Parameters

- `sidebar`: The view to show in the leading column.
- `detail`: The view to show in the detail area.

## See Also

- [init(sidebar: () -> Sidebar, content: () -> Content, detail: () -> Detail)](navigationsplitview/init(sidebar:content:detail:).md)
  Creates a three-column navigation split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitview/init(sidebar:detail:))*