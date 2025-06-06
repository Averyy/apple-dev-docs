# BalancedNavigationSplitViewStyle

**Framework**: SwiftUI  
**Kind**: struct

A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.

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
@preconcurrency struct BalancedNavigationSplitViewStyle
```

#### Overview

Use [`balanced`](navigationsplitviewstyle/balanced.md) to construct this style.

## Topics

### Creating the navigation split view style
- [init()](balancednavigationsplitviewstyle/init.md)
  Creates an instance of [`BalancedNavigationSplitViewStyle`](balancednavigationsplitviewstyle.md).

## Relationships

### Conforms To
- [NavigationSplitViewStyle](navigationsplitviewstyle.md)

## See Also

- [struct AutomaticNavigationSplitViewStyle](automaticnavigationsplitviewstyle.md)
  A navigation split style that resolves its appearance automatically based on the current context.
- [struct ProminentDetailNavigationSplitViewStyle](prominentdetailnavigationsplitviewstyle.md)
  A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.
- [struct NavigationSplitViewStyleConfiguration](navigationsplitviewstyleconfiguration.md)
  The properties of a navigation split view instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/balancednavigationsplitviewstyle)*