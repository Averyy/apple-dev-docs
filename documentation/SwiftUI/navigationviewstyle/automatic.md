# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default navigation view style in the current context of the view being styled.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Replace a styled [`NavigationView`](../navigationview.md) with a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
@export(implementation)
static var automatic: DefaultNavigationViewStyle { get }
```

Available when `Self` is `DefaultNavigationViewStyle`.

## See Also

### Getting built-in navigation view styles
- [static var columns: ColumnNavigationViewStyle](./columns.md)
  A navigation view style represented by a series of views in columns.
- [static var stack: StackNavigationViewStyle](./stack.md)
  A navigation view style represented by a view stack that only shows a single top view at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationviewstyle/automatic)*