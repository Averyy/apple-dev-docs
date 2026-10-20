# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A navigation split style that resolves its appearance automatically based on the current context.

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
@MainActor
@preconcurrency static var automatic: AutomaticNavigationSplitViewStyle { get }
```

Available when `Self` is `AutomaticNavigationSplitViewStyle`.

## See Also

### Creating built-in styles
- [static var balanced: BalancedNavigationSplitViewStyle](./balanced.md)
  A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [static var prominentDetail: ProminentDetailNavigationSplitViewStyle](./prominentdetail.md)
  A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitviewstyle/automatic)*