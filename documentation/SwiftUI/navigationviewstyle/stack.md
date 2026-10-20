# stack

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A navigation view style represented by a view stack that only shows a single top view at a time.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Replace a styled [`NavigationView`](../navigationview.md) with a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
@export(implementation)
static var stack: StackNavigationViewStyle { get }
```

Available when `Self` is `StackNavigationViewStyle`.

## Mentions

- [Migrating to new navigation types](../migrating-to-new-navigation-types.md)

## See Also

### Getting built-in navigation view styles
- [static var automatic: DefaultNavigationViewStyle](./automatic.md)
  The default navigation view style in the current context of the view being styled.
- [static var columns: ColumnNavigationViewStyle](./columns.md)
  A navigation view style represented by a series of views in columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationviewstyle/stack)*