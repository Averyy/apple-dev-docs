# NavigationSplitViewStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that specifies the appearance and interaction of navigation split views within a view hierarchy.

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
@preconcurrency protocol NavigationSplitViewStyle
```

#### Overview

To configure the navigation split view style for a view hierarchy, use the [`navigationSplitViewStyle(_:)`](view/navigationsplitviewstyle(_:).md) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Creating built-in styles
- [static var automatic: AutomaticNavigationSplitViewStyle](navigationsplitviewstyle/automatic.md)
  A navigation split style that resolves its appearance automatically based on the current context.
- [static var balanced: BalancedNavigationSplitViewStyle](navigationsplitviewstyle/balanced.md)
  A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [static var prominentDetail: ProminentDetailNavigationSplitViewStyle](navigationsplitviewstyle/prominentdetail.md)
  A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.
### Creating custom styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](navigationsplitviewstyle/makebody(configuration:).md)
  Creates a view that represents the body of a navigation split view.
- [NavigationSplitViewStyle.Configuration](navigationsplitviewstyle/configuration.md)
  The properties of a navigation split view instance.
- [associatedtype Body : View](navigationsplitviewstyle/body.md)
  A view that represents the body of a navigation split view.
### Supporting types
- [struct AutomaticNavigationSplitViewStyle](automaticnavigationsplitviewstyle.md)
  A navigation split style that resolves its appearance automatically based on the current context.
- [struct BalancedNavigationSplitViewStyle](balancednavigationsplitviewstyle.md)
  A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [struct ProminentDetailNavigationSplitViewStyle](prominentdetailnavigationsplitviewstyle.md)
  A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.
- [struct NavigationSplitViewStyleConfiguration](navigationsplitviewstyleconfiguration.md)
  The properties of a navigation split view instance.

## Relationships

### Conforming Types
- [AutomaticNavigationSplitViewStyle](automaticnavigationsplitviewstyle.md)
- [BalancedNavigationSplitViewStyle](balancednavigationsplitviewstyle.md)
- [ProminentDetailNavigationSplitViewStyle](prominentdetailnavigationsplitviewstyle.md)

## See Also

- [func navigationSplitViewStyle<S>(S) -> some View](view/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [protocol TabViewStyle](tabviewstyle.md)
  A specification for the appearance and interaction of a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitviewstyle)*