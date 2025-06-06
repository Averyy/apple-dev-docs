# automatic

**Framework**: SwiftUI  
**Kind**: property

Use the default leading column visibility for the current device.

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
static var automatic: NavigationSplitViewVisibility { get }
```

#### Discussion

This computed property returns one of the three concrete cases: [`detailOnly`](navigationsplitviewvisibility/detailonly.md), [`doubleColumn`](navigationsplitviewvisibility/doublecolumn.md), or [`all`](navigationsplitviewvisibility/all.md).

## See Also

- [static var all: NavigationSplitViewVisibility](navigationsplitviewvisibility/all.md)
  Show all the columns of a three-column navigation split view.
- [static var doubleColumn: NavigationSplitViewVisibility](navigationsplitviewvisibility/doublecolumn.md)
  Show the content column and detail area of a three-column navigation split view, or the sidebar column and detail area of a two-column navigation split view.
- [static var detailOnly: NavigationSplitViewVisibility](navigationsplitviewvisibility/detailonly.md)
  Hide the leading two columns of a three-column navigation split view, so that just the detail area shows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitviewvisibility/automatic)*